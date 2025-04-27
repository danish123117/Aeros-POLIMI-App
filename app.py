from flask import Flask , render_template, request, jsonify
from ngsiOperations.ngsildOperations.ngsildEntityCreator import*
from ngsiOperations.ngsildOperations.ngsildCrudOperations import*
from waitress import serve
from orionClient.orion_client import *
import threading
import queue
import os
from flask_cors import CORS
from datetime import datetime, timezone
import json
import requests
import logging

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)
app = Flask(__name__)

ORION_LD_URL = os.getenv("ORION_LD_URL", "localhost")
ORION_LD_PORT = os.getenv("ORION_LD_PORT", "1026")
CONTEXT_URL = os.getenv("CONTEXT_URL", "localhost")
CONTEXT_PORT = os.getenv("CONTEXT_PORT", "5051")
MADE_ORION_LD_URL = os.getenv("MADE_ORION_LD_URL", "localhost")
AGV_URL = os.getenv("AGV_URL", "localhost")
AGV_PORT = os.getenv("AGV_PORT", "5000")

def orderQuantity(order_list):
    order_qty = 0
    for order in order_list:
        qty = order.get("orderQuantity")
        if isinstance(qty, (int, float)):
            order_qty += qty
        else:
            logger.warning(f"Order {order.get('id')} is missing 'requestQty' or it is not a number.")
            continue
    return order_qty

def dispatch_agv(location):
    paylod = json.dumps({"location": location})
    url = f"http://{AGV_URL}:{AGV_PORT}/dispatch"
    try:
        response = requests.post(url ,data=paylod) # headers={"Content-Type": "application/json"
        if response.status_code == 200:
            logger.info("AGV dispatched successfully.")
            return True
        else:
            logger.error(f"Failed to dispatch AGV: {response.status_code} - {response.text}")
            return False
    except requests.RequestException as e:
        logger.error(f"Error dispatching AGV: {e}")
        return False


################Routes#######################
@app.route('/')
def home():
    incomplete_orders, processing_orders, completed_orders = extract_entity_data(ORION_LD_URL, ORION_LD_PORT, CONTEXT_URL, CONTEXT_PORT, ENTITY_TYPE="Order")
    return render_template("index.html", incomplete_orders=incomplete_orders, processing_orders=processing_orders, completed_orders=completed_orders)

@app.route('/incomplete_orders', methods=['GET'])
def display_incomplete_orders():
    # Fetch the entity from the NGSI-LD context broker
    orion = "localhost"
    orion_port = 1026

    order_entity = ngsi_get_current(
        entity="urn:ngsi-ld:order:order001",
        orion=orion,
        orion_port=orion_port,
        entity_type="order"
    )

    if order_entity:
        # Extract the incomplete orders list
        incomplete_orders = order_entity.get("incompleteOrderList", [])
    else:
        # If there's an error or no entity, set to empty and log the issue
        incomplete_orders = []
        print("Error fetching or parsing the entity.")

    # Render the HTML template with the incomplete orders data
    return render_template('incomplete_orders.html', orders=incomplete_orders)
@app.route('/complete_orders', methods=['GET'])
def display_complete_orders():
    # Fetch the entity from the NGSI-LD context broker
    orion = "localhost"
    orion_port = 1026

    order_entity = ngsi_get_current(
        entity="urn:ngsi-ld:order:order001",
        orion=orion,
        orion_port=orion_port,
        entity_type="order"
    )

    if order_entity:
        # Extract the incomplete orders list
        complete_orders = order_entity.get("completedOrderList", [])
    else:
        # If there's an error or no entity, set to empty and log the issue
        complete_orders = []
        print("Error fetching or parsing the entity.")

    # Render the HTML template with the incomplete orders data
    return render_template('complete_orders.html', orders=complete_orders)

@app.route("/start_production", methods=["POST"])
def start_production():
    data = request.get_json(silent=True) or {}
    mode = data.get("mode", "Baseline")
    n=4
    incomplete_orders, _, _ = extract_entity_data(ORION_LD_URL, ORION_LD_PORT, CONTEXT_URL, CONTEXT_PORT, ENTITY_TYPE="Order")
    print(f"Number of incomplete orders: {len(incomplete_orders)}")
    if len(incomplete_orders) != 0:
        for i in range(n):
            if orderQuantity(incomplete_orders[:i+1]) <= n: 
                print(f"Processing order {i+1} with quantity {orderQuantity(incomplete_orders[:i+1])}")
                continue
            else:
                break
        in_process_list = incomplete_orders[:i]
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")[:-2]
        response_patch =update_processing_order_list(in_process_list, ORION_LD_URL, ORION_LD_PORT, CONTEXT_URL, CONTEXT_PORT,timestamp)
        if response_patch:
            response_agv = dispatch_agv(location=1) # check how to fix if agv is not dispatched
            return jsonify({"success": True})
        else:
            return jsonify({"success": False})
        # if response_patch:
        #     return jsonify({"success": True})
        # else:
        #     return jsonify({"success": False})
    else:
        return jsonify({"Status": "No orders to process"})
    
@app.route("/complete_production", methods=["POST"])
def complete_production():
    global lea_order
    _, in_process_list, _ = extract_entity_data(ORION_LD_URL, ORION_LD_PORT, CONTEXT_URL, CONTEXT_PORT, ENTITY_TYPE="Order")
    if in_process_list:
        timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")[:-2]
        response = update_complete_order_list(in_process_list, ORION_LD_URL, ORION_LD_PORT, CONTEXT_URL, CONTEXT_PORT,timestamp)
        if response:
            response_agv = dispatch_agv(location=0)
            return jsonify({"success": True})
        else:
            return jsonify({"success": False})
    else:
        return jsonify({"Status": "No orders to complete"})

@app.route('/get_orders', methods=['GET'])# Done
def get_order():
    incomplete_orders, processing_orders, comleted_orders = extract_entity_data(ORION_LD_URL, ORION_LD_PORT, CONTEXT_URL, CONTEXT_PORT, ENTITY_TYPE="Order")
    return jsonify({"incomplete_orders": incomplete_orders, "processing_orders": processing_orders, "completed_orders": comleted_orders})

@app.route('/get_completed_orders', methods=['GET']) # Done
def get_order_info():
    _, _, comleted_orders = extract_entity_data(ORION_LD_URL, ORION_LD_PORT, CONTEXT_URL, CONTEXT_PORT, ENTITY_TYPE="Order")
    return jsonify({"completed_orders": comleted_orders})

@app.route('/history', methods=['GET'])#
def history():
    _, _, comleted_orders = extract_entity_data(ORION_LD_URL, ORION_LD_PORT, CONTEXT_URL, CONTEXT_PORT, ENTITY_TYPE="Order")
    return render_template("history.html", completed_orders=comleted_orders)

if __name__ == "__main__":
    serve(app, host= "0.0.0.0", port= 3005)


