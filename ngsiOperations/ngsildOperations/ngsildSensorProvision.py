import requests
 

def sensor_provision_UC2(iota_container_name,iota_container_port,orion, orion_port):
# provision service path
    url = f'http://{iota_container_name}:{iota_container_port}/iot/services'
    headers = {
        'Content-Type': 'application/json',
        'fiware-service': 'openiot',
        'fiware-servicepath': '/'
    }
    data = {
        "services": [
            {
                "apikey": "danishabbas1",
                "cbroker": f"http://{orion}:{orion_port}",
                "entity_type": "sEMG",
                "resource": "",
                "transport": "MQTT",
                "attributes": [
                    {"object_id": "timeStamp", "name": "timeStamp", "type": "Property"},
                    {"object_id": "data", "name": "data", "type": "Property"},
                    {"object_id": "index", "name": "index", "type": "Property"},
                    {"object_id": "feaisability", "name": "feaisability", "type": "Property"}]
               
            },
            {
                "apikey": "danishabbas2",
                "cbroker": f"http://{orion}:{orion_port}",
                "entity_type": "PolarH10TopicECG",
                "resource": "",
                "transport": "MQTT",
                "attributes": [
                    {"object_id": "timeStamp", "name": "timeStamp", "type": "Property"},
                    {"object_id": "sensorTimeStamp", "name": "sensorTimeStamp", "type": "Property"},
                    {"object_id": "ecg", "name": "ecg", "type": "Property"},
                    {"object_id": "sessionId", "name": "sessionId", "type": "Property"}
                    ],
                "static_attributes": [
                    {"object_id": "clientId", "name": "clientId", "type": "Property"},
                    {"object_id": "deviceId", "name": "deviceId", "type": "Property"},
                    {"object_id": "sampleRate", "name": "sampleRate", "type": "Property"}                    

                ]
            },
            {
                "apikey": "danishabbas2",
                "cbroker": f"http://{orion}:{orion_port}",
                "entity_type": "PolarH10TopicACC",
                "resource": "",
                "transport": "MQTT",
                "attributes": [
                    {"object_id": "timeStamp", "name": "timeStamp", "type": "Property"},
                    {"object_id": "sensorTimeStamp", "name": "sensorTimeStamp", "type": "Property"},
                    {"object_id": "acc", "name": "acc", "type": "Property"},
                    {"object_id": "sessionId", "name": "sessionId", "type": "Property"},
                    {"object_id": "sampleRate", "name": "sampleRate", "type": "Property"}
                ],
                "static_attributes": [
                    {"object_id": "clientId", "name": "clientId", "type": "Property"},
                    {"object_id": "deviceId", "name": "deviceId", "type": "Property"},
                ]
            },
            {
                "apikey": "danishabbas2",
                "cbroker": f"http://{orion}:{orion_port}",
                "entity_type": "PolarH10TopicHR",
                "resource": "",
                "transport": "MQTT",
                "attributes": [
                    {"object_id": "timeStamp", "name": "timeStamp", "type": "Property"},
                    {"object_id": "sensorTimeStamp", "name": "sensorTimeStamp", "type": "Property"},
                    {"object_id": "hr", "name": "hr", "type": "Property"},
                    {"object_id": "hrv", "name": "hrv", "type": "Property"},
                    {"object_id": "rr", "name": "rr", "type": "Property"},                    
                    {"object_id": "sessionId", "name": "sessionId", "type": "Property"},

                ],
                "static_attributes": [
                    {"object_id": "clientId", "name": "clientId", "type": "Property"},
                    {"object_id": "deviceId", "name": "deviceId", "type": "Property"},
                    {"object_id": "sampleRate", "name": "sampleRate", "type": "Property"}
                ]
            }
        ]
    }

    servicepath_provision_response = requests.post(url, json=data, headers=headers)
    #print(servicepath_response.status_code)
    #print(servicepath_response.text)
    #provision EMG sensor
    url = f'http://{iota_container_name}:{iota_container_port}/iot/devices'
    headers = {
        'Content-Type': 'application/json',
        'fiware-service': 'openiot',
        'fiware-servicepath': '/'
    }
    data = {
        "devices": [
            {
                "device_id": "sEMG",
                "entity_name": "urn:ngsi-ld:sEMG:EMG1000",
                "entity_type": "sEMG",
                "attributes": [
                    {"object_id": "timeStamp", "name": "timeStamp", "type": "Property"},
                    {"object_id": "data", "name": "data", "type": "Property"},
                    {"object_id": "index", "name": "index", "type": "Property"},
                    {"object_id": "feaisability", "name": "feaisability", "type": "Property"}]
            },
                        {
                "device_id": "ecg",
                "entity_name": "urn:ngsi-ld:PolarH10TopicECG:001",
                "entity_type": "PolarH10TopicECG",
                "attributes": [
                    {"object_id": "timeStamp", "name": "timeStamp", "type": "Property"},
                    {"object_id": "sensorTimeStamp", "name": "sensorTimeStamp", "type": "Property"},
                    {"object_id": "ecg", "name": "ecg", "type": "Property"},
                    {"object_id": "sessionId", "name": "sessionId", "type": "Property"}
                    ],
                "static_attributes": [
                    {"object_id": "clientId", "name": "clientId", "type": "Property"},
                    {"object_id": "deviceId", "name": "deviceId", "type": "Property"},
                    {"object_id": "sampleRate", "name": "sampleRate", "type": "Property"}                    

                ]
            },
                        {
                "device_id": "hr",
                "entity_name": "urn:ngsi-ld:PolarH10TopicHR:001",
                "entity_type": "PolarH10TopicHR",
                "attributes": [
                    {"object_id": "timeStamp", "name": "timeStamp", "type": "Property"},
                    {"object_id": "sensorTimeStamp", "name": "sensorTimeStamp", "type": "Property"},
                    {"object_id": "hr", "name": "hr", "type": "Property"},
                    {"object_id": "hrv", "name": "hrv", "type": "Property"},
                    {"object_id": "rr", "name": "rr", "type": "Property"},                    
                    {"object_id": "sessionId", "name": "sessionId", "type": "Property"},

                ],
                "static_attributes": [
                    {"object_id": "clientId", "name": "clientId", "type": "Property"},
                    {"object_id": "deviceId", "name": "deviceId", "type": "Property"},
                    {"object_id": "sampleRate", "name": "sampleRate", "type": "Property"}
                ]

            },
                        {
                "device_id": "acc",
                "entity_name": "urn:ngsi-ld:PolarH10TopicACC:001",
                "entity_type": "PolarH10TopicACC",
                "attributes": [
                    {"object_id": "timeStamp", "name": "timeStamp", "type": "Property"},
                    {"object_id": "sensorTimeStamp", "name": "sensorTimeStamp", "type": "Property"},
                    {"object_id": "acc", "name": "acc", "type": "Property"},
                    {"object_id": "sessionId", "name": "sessionId", "type": "Property"},
                    {"object_id": "sampleRate", "name": "sampleRate", "type": "Property"}
                ],
                "static_attributes": [
                    {"object_id": "clientId", "name": "clientId", "type": "Property"},
                    {"object_id": "deviceId", "name": "deviceId", "type": "Property"},
                ]
            }


        ]
    }
    sensor_provision_response = requests.post(url, json=data, headers=headers)
    #print(sensor_response.status_code)
    #print(sensor_response.text)
    return servicepath_provision_response , sensor_provision_response

def sensor_provision_UC1(iota_container_name,iota_container_port,orion, orion_port):

    #print(servicepath_response.status_code)
    #print(servicepath_response.text)
    #provision EMG sensor
    #url = 'http://iot-agent:4041/iot/devices'
    #url = 'http://localhost:4041/iot/devices'
    url = f'http://{iota_container_name}:{iota_container_port}/iot/devices'
    headers = {
        'Content-Type': 'application/json',  
        'fiware-service': 'openiot', 
        'fiware-servicepath': '/'    
    }
    data = {
        "devices": [
            {
                "device_id": "EMG1000",
                "entity_name": "urn:ngsi-ld:sEMG:EMG1000",
                "entity_type": "sEMG",
                "attributes": [
                    {"object_id": "timeStamp", "name": "timeStamp", "type": "Property"},
                    {"object_id": "data", "name": "data", "type": "Property"},
                    {"object_id": "index", "name": "index", "type": "Property"},
                    {"object_id": "feaisability", "name": "feaisability", "type": "Property"}]
            }
        ]
    }
    sensor_provision_response = requests.post(url, json=data, headers=headers)
    #print(sensor_response.status_code)
    #print(sensor_response.text)
    # provision service path
    #url = 'http://iot-agent:4041/iot/services'
    #url = 'http://localhost:4041/iot/services'
    url = f'http://{iota_container_name}:{iota_container_port}/iot/services'
    headers = {
        'Content-Type': 'application/json',
        'fiware-service': 'openiot',
        'fiware-servicepath': '/'

    }
    data = {
        "services": [
            {
                "apikey": "danishabbas1",
                "cbroker": f"http://{orion}:{orion_port}",
                 #"cbroker": "http://orion:1026",               
                "entity_type": "sEMG",
                "resource": "",
                "transport": "MQTT",
                "attributes": [
                    {"object_id": "timeStamp", "name": "timeStamp", "type": "Property"},
                    {"object_id": "data", "name": "data", "type": "Property"},
                    {"object_id": "index", "name": "index", "type": "Property"},
                    {"object_id": "feaisability", "name": "feaisability", "type": "Property"}]
               
            }
        ]     
        
    }

    servicepath_provision_response = requests.post(url, json=data, headers=headers)
    
    return servicepath_provision_response , sensor_provision_response

def sensor_prov_kill(device_id,api_key,iota_container_name,iota_container_port ): 
    # kill sensor provision
    url_s = f"http://{iota_container_name}:{iota_container_port}/iot/devices/{device_id}"
    url_p = f"http://{iota_container_name}:{iota_container_port}/iot/services/?resource=&apikey={api_key}"
    payload = ""
    headers = {
    'Content-Type': 'application/json',
    'fiware-service': 'openiot',
    'fiware-servicepath': '/'
    }
    response_s = requests.request("DELETE", url_s, headers=headers, data=payload)
      
    response_p = requests.request("DELETE", url_p, headers=headers, data=payload)

    return response_s, response_p