class CoAPClient:
    def __init__(self, connector):
        self.connector = connector

    def getServerStatus(self, pathToSource):

        try:
            response = self.connector.get(pathToSource)
            print(f"GET {pathToSource}: {response.code} - {response.payload}")
            return response
        except Exception as e:
            print(f"Erorr GET: {e}")
            return None
    
    def sentSestData(self, pathToSource, testData):
        pass
    

