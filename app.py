from flask import Flask , render_template, request
from ngsiOperations.ngsildOperations.ngsildEntityCreator import*
from ngsiOperations.ngsildOperations.ngsildSensorProvision import*
from ngsiOperations.ngsildOperations.ngsildCrudOperations import*
#from ngsiOperations.ngsildOperations.ngsildSubscriptions import createSubscriptions
from waitress import serve
import threading
import queue
import os

app = Flask(__name__)

@app.route('/')
@app.route('/index')

def index():
    return render_template('index.html')

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

@app.route('/get_rawmaterials')
def getrawmat():
    print('this downloads the data of a trial')

@app.route('/dispatch_order')
def dispatchmaterial():
    print('this downloads the data of a trial')
    
@app.route('/setup')
def initial_setup():
    orion= "localhost"
    port=1026
    context="context"
    d1 ={
    "id": "urn:ngsi-ld:order:order002",
    "type": "order",
        "incompleteOrderList": {
            "type": "Property",
            "value": [["1004","2024-01-16T17:50:07.5870Z",5],["1005","2024-01-16T17:51:07.5870Z",4]]
        },
        "processingOrderList": {
            "type": "Property",
            "value": []
        },
        "completedOrderList": {
            "type": "Property",
            "value": [["1001","2024-01-16T17:50:07.5870Z",4],["1002","2024-01-16T17:51:07.5870Z",1]]
        }
    }
    r2 = ngsi_create_entity(d1,orion="localhost",orion_port=1026,context="context",context_port=5051)
    print(r2.status_code)
    return r2

if __name__ == "__main__":
    serve(app, host= "0.0.0.0", port= 3005)


