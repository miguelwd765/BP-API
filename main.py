import requests
import json
import creds


# function to run GET to retrieve categories

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
    
    #print all category names and ids to user
    data = response.get("response")
    
    for d in data:
        catId = d["id"]
        catName = d["name"]
        print(f"The category ID for {catName} is {catId}")
    
getCategoryIds("use1", "mpachecotest")

# function to run PUT request based on user input

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
    
    # complete PUT request and prints out message to user
    
    response = requests.put(url=url, headers=headers, json=body)
    response = response.status_code
    if response == 200:
        print(f"Successfully updated sub category to ID: {userCategory}!!!!")
    else:
        print(f"Something went wrong {response}")
    
updateProducts("use1", "mpachecotest")