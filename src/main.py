from dotenv import dotenv_values
from util.CoAPPropFileSearcher import serchCoAPProperties
from CoAP.SyncCoAPConnector import SyncCoAPConnector
from CoAP.CoAPClient import CoAPClient


def main():

    coapPropFile = serchCoAPProperties()
    confs = dotenv_values(coapPropFile)

    if confs == None:
        raise FileNotFoundError("Error: The configuration file '*.coap.properties' was not found!")

    coapConnection = SyncCoAPConnector(confs.get("COAP_HOST"), int(confs.get("COAP_PORT")))
    coapConnection.connect()

    client = CoAPClient(coapConnection.getConnect())
    client.getServerStatus(confs.get("COAP_SOURCE"))



if __name__ == '__main__':
    main()