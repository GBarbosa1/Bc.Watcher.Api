from fastapi import FastAPI
from api.getIpcaTotal import getIpcaTotal
from Json.JsonHandler import json_load

app = FastAPI()

@app.get("/Ipca/PrecosMonitoradosTotal")
def read_item():
    try:
        responseRaw, lasIpca, statusCode = getIpcaTotal()
        return lasIpca
    except Exception as error:
        errorCode = "Failed to realize action the error is :"+str(error)
        return errorCode
    
@app.get("/Ipca/PrecosMonitoradosTotal/raw")
def read_item():
    try:
        responseRaw, lasIpca, statusCode = getIpcaTotal()
        return responseRaw
    except Exception as error:
        errorCode = "Failed to realize action the return status from BC API were: "+str(statusCode)
        return errorCode
    