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
    
    catParents = {}
    
    for d in data:
        catParent = d.get("parentId", 0)
        catId = d["id"]
        catName = d["name"]
        catParents[catId] = catParent
        print(f"The category ID for {catName} is {catId}")
        
    
    # user Inputs
    
    userCategory = int(input("Using the above ^^^ type in the ID of the CATEGORY you want to assign products to: "))
    
    # store parent category based off user input in dictionary to use for body2
    
    userCatParent = int(catParents.get(userCategory, None))
    
    body = {
        "reporting": {
            "subcategoryId": userCategory
		}
    }
    
    data = {
        "reporting": {
            "categoryId": userCatParent,
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
    
    if userCatParent == 0:
        response = requests.put(url=url, headers=headers, json=body)
        # print("Request body:", json.dumps(body, indent=2))
    elif userCatParent != 0:
        # print("Request body:", json.dumps(data, indent=2))
        response = requests.put(url=url, headers=headers, json=data)
    else:
        print("Something went wrong!!")
   
    # print request that is being sent
        
    # print("Request URL:", url)
    # print("Request Headers:", headers)
    # print("Request Body:", json.dumps(data, indent=2))
    
    response = response.status_code
    if response == 200:
        print(f"Successfully updated sub category to ID: {userCategory}!!!!")
    else:
        print(f"Something went wrong {response}")
    
getCategoryIds("use1", "mpachecotest")