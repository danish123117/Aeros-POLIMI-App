import requests
import json
def ngsi_create_entity(d,orion,orion_port,context,context_port=5051):#updates latest values
    url = f'http://{orion}:{orion_port}/ngsi-ld/v1/entities/'
    #url = 'http://localhost:1026/ngsi-ld/v1/entityOperations/create'
    headers = {
  'Link': f'<http://{context}:{context_port}/ngsi-context.jsonld>; rel="http://www.w3.org/ns/json-ld#context"; type="application/ld+json"',
  'Content-Type': 'application/json'
}
    payload = json.dumps(d)
    response = requests.request("POST", url, headers=headers, data=payload)
    return response
 
def ngsi_create_trial_UC2(trial_name,orion,orion_port,context):
    d_stress = {
    "id": "urn:ngsi-ld:EmgFrequencyDomainFeatures:001",
    "type": "EmgFrequencyDomainFeatures",
    "trialName":trial_name,
    "medianFrequencyState": {
      "type": "Property",
      "value": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]},
    "meanFrequencyState": {
      "type": "Property",
      "value": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] },
    "meanPowerFrequencyState": {
      "type": "Property",
      "value": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]},
    "zeroCrossingFrequencyState": {
      "type": "Property",
      "value": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}
     }  
    d_emg = {
    "id": "urn:ngsi-ld:sEMG:EMG1000",
    "type": "sEMG",
    "trialName":trial_name,
    "timeStamp": {
      "type": "Property",
      "value": "132"
    },
    "index": {
      "type": "Property",
      "value": 0
    },
    "data":{
      "type":"Property",
      "value":[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
              },
    "feaisability":{
      "type":"Property",
      "value":[True,True,True,True,True,True,True,True]}
    }
    ar = 73*[0]
    d_ecg = {
    "id": "urn:ngsi-ld:PolarH10TopicECG:001",
    "type": "PolarH10TopicECG",
    "trialName":trial_name,
    "clientId": {
      "type": "Property",
      "value": "0000"
      },
    "deviceId": {
      "type": "Property",
      "value": "0000"
      },
    "sessionId":{
      "type":"Property",
      "value":0
      },
    "timeStamp":{
      "type":"Property",
      "value":0
      },
    "sampleRate":{
      "type":"Property",
      "value":130
      },
    "sensorTimeStamp":{
      "type":"Property",
      "value":0
      },
    "ecg":{
      "type":"Property",
      "value":ar
      }
    }

    d_hr = {
    "id": "urn:ngsi-ld:PolarH10TopicHR:001",
    "type": "PolarH10TopicHR",
    "trialName":trial_name,
    "clientId": {
      "type": "Property",
      "value": "0000"
      },
    "deviceId": {
      "type": "Property",
      "value": "0000"
      },
    "sessionId":{
      "type":"Property",
      "value":0
      },
    "timeStamp":{
      "type":"Property",
      "value":0
      },
    "sensorTimeStamp":{
      "type":"Property",
      "value":0
      },
    "hr":{
      "type":"Property",
      "value":0
      },
    "hrv":{
      "type":"Property",
      "value":0
      },
    "rr":{
      "type":"Property",
      "value":[0]
      }
    }
    ac = [[0,0,0]]*36
    d_acc = {
    "id": "urn:ngsi-ld:PolarH10TopicACC:001",
    "type": "PolarH10TopicACC",
    "trialName":trial_name,
    "clientId": {
      "type": "Property",
      "value": "0000"
      },
    "deviceId": {
      "type": "Property",
      "value": "0000"
      },
    "sessionId":{
      "type":"Property",
      "value":0
      },
    "timeStamp":{
      "type":"Property",
      "value":0
      },
    "sampleRate":{
      "type":"Property",
      "value":25
      },
    "sensorTimeStamp":{
      "type":"Property",
      "value":0
      },
    "acc":{
      "type":"Property",
      "value":ac
      }
    }
    payload = json.dumps([d_stress,d_emg,d_acc,d_ecg,d_hr])
    resp= ngsi_create_entity(payload,orion,orion_port,context)
    return resp

def ngsi_create_trial_UC1(trial_name,orion,orion_port,context):
    d_stress = {
    "id": "urn:ngsi-ld:EmgFrequencyDomainFeatures:001",
    "type": "EmgFrequencyDomainFeatures",
    "trialName":trial_name,
    "medianFrequencyState": {
      "type": "Property",
      "value": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]},
    "meanFrequencyState": {
      "type": "Property",
      "value": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] },
    "meanPowerFrequencyState": {
      "type": "Property",
      "value": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]},
    "zeroCrossingFrequencyState": {
      "type": "Property",
      "value": [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]}
     }  
    d_emg = {
    "id": "urn:ngsi-ld:sEMG:EMG1000",
    "type": "sEMG",
    "trialName":trial_name,
    "timeStamp": {
      "type": "Property",
      "value": "132"
    },
    "index": {
      "type": "Property",
      "value": 0
    },
    "data":{
      "type":"Property",
      "value":[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
              },
    "feaisability":{
      "type":"Property",
      "value":[True,True,True,True,True,True,True,True]}
    }
    payload = json.dumps([d_stress,d_emg])

    resp= ngsi_create_entity(payload,orion,orion_port,context)
    return resp

#Done