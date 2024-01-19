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

def updateProducts(server, account):
    # user Inputs
    userCategory = input("Using the above ^^^ type in the ID of the CATEGORY you want to assign products to: ")
    body = {
        "reporting": {
        "subcategoryId": userCategory
		}
    }
    userProducts = input("Which products do you want to assign to this category?")
    # build out URI
    url = "https://%s.brightpearlconnect.com/public-api/%s/product-service/product/%s" % (server, account, userProducts)
    
    headers = {
        "content-type": "application/json",
        "brightpearl-app-ref": creds.app_ref,
        "brightpearl-account-token": creds.api_key
    }
    
    response = requests.put(url=url, headers=headers, json=body)
    print(response)
    
updateProducts("use1", "mpachecotest")