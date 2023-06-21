from fastapi import FastAPI
from api.getIpcaTotal import getIpcaTotal
from api.getIpcaBensDuraveis import getIpcaBensDuraveis
from api.getIpcaBensNaoDuraveis import getIpcaBensNaoDuraveis
from api.getIpcaServicos import getIpcaServicos
from Json.JsonHandler import json_load
from scrap.scrap_engine import scrap_init, get_url,get_element_xpath, strip

app = FastAPI()

@app.get("/Ipca/PrecosMonitoradosTotal")
def preco_amplo_total():
    try:
        ipca, statusCode = getIpcaTotal()
        return ipca
    except Exception as error:
        errorCode = "Failed to realize action the error is: "+str(error)
        return errorCode
    

@app.get("/Ipca/BensDuraveis")
def preco_bens_duraveis():
    try:
        ipca, statusCode = getIpcaBensDuraveis()
        return ipca
    except Exception as error:
        errorCode = "Failed to realize action the error is: "+str(error)
        return errorCode
    
@app.get("/Ipca/BensNaoDuraveis")
def preco_bens_nao_duraveis():
    try:
        ipca, statusCode = getIpcaBensNaoDuraveis()
        return ipca
    except Exception as error:
        errorCode = "Failed to realize action the error is: "+str(error)
        return errorCode
    
@app.get("/Ipca/Servicos")
def servicos():
    try:
        ipca, statusCode = getIpcaServicos()
        return ipca
    except Exception as error:
        errorCode = "Failed to realize action the error is: "+str(error)
        return errorCode
    
@app.get("/ata")
def servicos():
    try:
        settings = json_load("settings\settings.json")
        url = settings["scrapUrls"][0]["ataDoCopom"]
        browser = scrap_init(url)
        dateElement = get_element_xpath(browser, settings["scrapUrls"][0]["ataCopomDateXpath"])
        date = strip(dateElement)
        #needs to strip the download button url
        return ipca
    except Exception as error:
        errorCode = "Failed to realize action the error is: "+str(error)
        return errorCode
    
