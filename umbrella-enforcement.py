

"""
UMBRELLA ENFORCEMENT API DEMO
"""
import requests
import json


"""
Key can be seen here:
https://dashboard.umbrella.com/o/<ORGID>/#/policies/components/thirdpartyintegrations

"""
key="1111-2222-3333-4444"

get_url = "https://s-platform.api.opendns.com/1.0/domains?customerKey="+key
headers = {
  'Content-Type': 'application/json'
}

print("Get the list:")
response = requests.request("GET", get_url, headers=headers)
print(response.text)

print("Add new entry:")
url = "https://s-platform.api.opendns.com/1.0/events?customerKey="+key
payload = json.dumps([
  {
    "alertTime": "2020-10-02T12:18:19.458Z",
    "deviceId": "ba6a59f4-e692-4724-ba36-c28132c761de",
    "deviceVersion": "13.7a",
    "dstDomain": "retdemos3.com",
    "dstUrl": "retdemos3.com",
    "eventTime": "2020-10-02T12:18:19.458Z",
    "protocolVersion": "1.0a",
    "providerName": "Security Platform"
  }
])
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)