from dotenv import dotenv_values
from util.CoAPPropFileSearcher import serchCoAPProperties
from CoAP.SyncCoAPConnector import SyncCoAPConnector
from CoAP.CoAPClient import CoAPClient

import cbor2


def main():

    coapPropFile = serchCoAPProperties()
    confs = dotenv_values(coapPropFile)

    if confs == None:
        raise FileNotFoundError("Error: The configuration file '*.coap.properties' was not found!")

    coapConnection = SyncCoAPConnector(confs.get("COAP_HOST"), int(confs.get("COAP_PORT")))
    coapConnection.connect()

    client = CoAPClient(coapConnection.getConnect(), confs.get("COAP_HOST"), int(confs.get("COAP_PORT")))

    #------Temp Form---------------

    # client.getServerStatus(confs.get("COAP_SOURCE"))

    # deviceData = {    
    #     "device_name": "ID_2F13433HFG12",       
    #     "device_latitude": 55.755831, 
    #     "device_longitude": 37.617673
    # }

    # testedData = {
    #     "device_id":1,
    #     "train_data_timestamp_input": [2025, 9, 12, 10, 52, 43],
    #     "wheel_count_rail_input": 145,
    #     "wheel_speed_rail_input": 1245,
    #     "train_data_timestamp_output": [0, 0, 0, 0, 0, 0,],
    #     "wheel_count_rail_output": 0,
    #     "wheel_speed_rail_output": 0,
    #     "common_Count_trains_entering_railway": 1,
    #     "common_Count_train_wheels_entering_railway": 145
    # }

    # cbor_data = cbor2.dumps(testedData)

    # decoded_data = cbor2.loads(cbor_data)

    # client.sendPOSTRequest(confs.get("COAP_SOURCE"), cbor_data)



if __name__ == '__main__':
    main()