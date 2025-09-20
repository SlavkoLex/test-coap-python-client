from coapthon.messages.request import Request
from coapthon import defines

import cbor2

class CoAPClient:
    def __init__(self, connector, host, port):
        self.connector = connector
        self.host = host
        self.port = port

    def getServerStatus(self, pathToSource):

        try:
            response = self.connector.get(pathToSource)
            print(f"GET {pathToSource}: {response.code} - {response.payload}")
            return response
        except Exception as e:
            print(f"Erorr GET: {e}")
            return None
    
    def sendPOSTRequest(self, pathToSource, rowData):
            request = Request()
            request.destination = (self.host, self.port)
            request.code = defines.Codes.POST.number
            request.uri_path = pathToSource
            request.payload = rowData.hex()
            request.content_type = defines.Content_types["application/cbor"]
            self.connector.send_request(request)

    

