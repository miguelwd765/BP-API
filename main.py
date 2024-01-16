import requests
import json
import creds

def getCategoryIds(server, account):
     # build out URI
    url = "https://%s.brightpearlconnect.com/public-api/%s/product-service/brightpearl-category/" % (server, account)
    
     # add headers
    headers = {
        "content-type": "application/json",
        "brightpearl-app-ref": creds.app_ref,
        "brightpearl-account-token": creds.api_key
    }
    
    response = requests.get(url=url, headers=headers).json()
    
    data = response.get("response")
    
    for d in data:
        catId = d["id"]
        catName = d["name"]
        print(f"The category ID for {catName} is {catId}")
    
getCategoryIds("use1", "mpachecotest")