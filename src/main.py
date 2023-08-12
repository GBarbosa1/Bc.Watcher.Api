from fastapi import FastAPI
from api.getIpca import getIpcaTotal, getIpcaBensDuraveis, getIpcaBensNaoDuraveis, getIpcaServicos
from Json.JsonHandler import json_load
from scrap.scrap_engine import scrap_init, get_url,get_element_xpath, strip
import requests
from pydantic import BaseModel
import uvicorn
import time

app = FastAPI()

class Message(BaseModel):
    text: str
    
@app.get("/")
def preco_amplo_total():
    return("Hello world!")
    

@app.get("/Ipca/PrecosMonitoradosTotal/{last}")
def preco_amplo_total(last:str):
    try:
        ipca, statusCode = getIpcaTotal(last)
        return ipca
    except Exception as error:
        errorCode = "Failed to realize action the error is: "+str(error)
        return errorCode
    

@app.get("/Ipca/BensDuraveis/{last}")
def preco_bens_duraveis(last:str):
    try:
        ipca, statusCode = getIpcaBensDuraveis(last)
        return ipca
    except Exception as error:
        errorCode = "Failed to realize action the error is: "+str(error)
        return errorCode
    
@app.get("/Ipca/BensNaoDuraveis/{last}")
def preco_bens_nao_duraveis(last:str):
    try:
        ipca, statusCode = getIpcaBensNaoDuraveis(last)
        return ipca
    except Exception as error:
        errorCode = "Failed to realize action the error is: "+str(error)
        return errorCode
    
@app.get("/Ipca/Servicos/{last}")
def servicos(last:str):
    try:
        ipca, statusCode = getIpcaServicos(last)
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
        time.sleep(5)
        dateElement = get_element_xpath(browser, settings["scrapUrls"][0]["ataCopomDateXpath"])
        print(settings["scrapUrls"][0]["ataCopomDateXpath"])
        date = strip(dateElement)
        return date
    except Exception as error:
        errorCode = "Failed to realize action the error is: "+str(error)
        return errorCode
    
@app.get("/recorddownloadlink")
def servicos():
    try:
        settings = json_load("settings\settings.json")
        url = settings["scrapUrls"][0]["ataDoCopom"]
        browser = scrap_init(url)
        time.sleep(5)
        downloadElement = get_element_xpath(browser, settings["scrapUrls"][0]["ataDownloadXPath"])
        downloadElement = downloadElement.get_attribute('href')
        return downloadElement
    except Exception as error:
        errorCode = "Failed to realize action the error is: "+str(error)
        return errorCode

@app.post("/sendmessage")
def message(telegram_text:Message):
    HTTP_API_TOKEN = ""
    CHAT_ID = ""
    MESSAGE_TEXT = telegram_text.text
    URL = f"https://api.telegram.org/bot{HTTP_API_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={MESSAGE_TEXT}"
    response = requests.post(URL).json()
    return response, URL

if __name__ == "__main__":
    uvicorn.run(app, host = "127.0.0.1", port=8000)