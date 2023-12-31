import requests
from Json.JsonHandler import json_load

def getIpcaTotal(last): 
    url = json_load("settings\settings.json")
    url = url["apisUrls"][0]["precosMonitoradosTotal"] + str(last)
    payload = {}
    headers = {
  'Cookie': 'TS01912a8f=012e4f88b3a33f2f53565e14e26cd36756b4132ca1771059e2adf7106982ed3efc921b4475ec19e7536368304b2030c9581a12f418; cookie_p=!a1knjzPIfOa67sQdwXJzSPVoLSm8xZVaNYGetEMf24D97hMm3Kv+KsOOqGt3NjZbfsbbvsBTWwBgJ2Y='
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json(), response.status_code

def getIpcaBensDuraveis(last): 
    url = json_load("settings\settings.json") 
    url = url["apisUrls"][0]["precosAoConsumidorBensDuraveis"] + str(last)
    payload = {}
    headers = {
  'Cookie': 'TS01912a8f=012e4f88b3a33f2f53565e14e26cd36756b4132ca1771059e2adf7106982ed3efc921b4475ec19e7536368304b2030c9581a12f418; cookie_p=!a1knjzPIfOa67sQdwXJzSPVoLSm8xZVaNYGetEMf24D97hMm3Kv+KsOOqGt3NjZbfsbbvsBTWwBgJ2Y='
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json(), response.status_code
  
def getIpcaBensNaoDuraveis(last): 
    url = json_load("settings\settings.json") 
    url = url["apisUrls"][0]["precosAoConsumidorBensNaoDuraveis"] + str(last)
    payload = {}
    headers = {
  'Cookie': 'TS01912a8f=012e4f88b3a33f2f53565e14e26cd36756b4132ca1771059e2adf7106982ed3efc921b4475ec19e7536368304b2030c9581a12f418; cookie_p=!a1knjzPIfOa67sQdwXJzSPVoLSm8xZVaNYGetEMf24D97hMm3Kv+KsOOqGt3NjZbfsbbvsBTWwBgJ2Y='
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json(), response.status_code

def getIpcaServicos(last): 
    url = json_load("settings\settings.json")
    url = url["apisUrls"][0]["precoAoConsumidorServicos"] + str(last)
    payload = {}
    headers = {
  'Cookie': 'TS01912a8f=012e4f88b3a33f2f53565e14e26cd36756b4132ca1771059e2adf7106982ed3efc921b4475ec19e7536368304b2030c9581a12f418; cookie_p=!a1knjzPIfOa67sQdwXJzSPVoLSm8xZVaNYGetEMf24D97hMm3Kv+KsOOqGt3NjZbfsbbvsBTWwBgJ2Y='
    }
    response = requests.request("GET", url, headers=headers, data=payload)
    return response.json(), response.status_code