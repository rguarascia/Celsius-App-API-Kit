import requests
import json
from .const import PATHS

def readCreds(pathToCreds):
    userSecret = json.load(open(pathToCreds))
    return userSecret

def responseHandler(response):
    if response.status_code == 200:
        return json.loads(response.text)
    else:
        return response

def getBalance(userSecret):
    response = requests.get(PATHS["baseURL"] + PATHS["balanceSummary"], headers = userSecret)        
    return responseHandler(response)
        
def getInterest(userSecret):
    response = requests.get(PATHS["baseURL"] + PATHS["interestSummary"], headers = userSecret)
    return responseHandler(response)
    
def getStats(userSecret):
    response = requests.get(PATHS["baseURL"] + PATHS["statistics"], headers = userSecret)
    return responseHandler(response)

def getTransactions(userSecret, pages):
    response = requests.get(PATHS["baseURL"] + PATHS["transactionSummary"], headers = userSecret, params = pages)
    return responseHandler(response)