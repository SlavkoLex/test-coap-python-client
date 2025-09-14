from coapthon.client.helperclient import HelperClient

class SyncCoAPConnector:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.connection = None

    def connect(self):
        self.connection = HelperClient(server=(self.host, self.port))

    def getConnect(self):
        return self.connection
