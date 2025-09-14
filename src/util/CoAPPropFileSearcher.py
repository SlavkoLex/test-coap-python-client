from pathlib import Path

def serchCoAPProperties():

    dirName = "./src"
    fileName = "*.coap.properties"
    coapFile = None 

    startDir = Path(dirName)
    for filePath in startDir.rglob(fileName):
        if filePath.is_file():
            coapFile = filePath
            break
    
    return coapFile
