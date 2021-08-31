#!/usr/bin/env python

"""
TEST:
curl -i -X POST "https://management.api.umbrella.com/v1/organizations/<ORGID>/internaldomains" \
-H 'Authorization: Basic <TOKEN>' \
-H 'Content-Type: application/json' \
-d '{ "domain": "Dtest" }'
"""
import requests
import base64

OrgID="<ORGID>"
url="https://management.api.umbrella.com/v1/organizations/"
api_key=".."
api_secret="..."
# Substitute your key and secret.
keySecret = api_key+":"+api_secret

# Encode and print your credentials
token = base64.b64encode(keySecret.encode())
encoding = 'utf-8'
payload='{ "domain": "Dtest3", "description":"Dtest3","includeAllVAs":false,"includeAllMobileDevices":false }'
headers = {
  'Authorization': 'Basic '+str(token, encoding),
  'Content-Type': 'application/json'
}

url_domains= url + OrgID+"/internaldomains"
response = requests.request("POST", url_domains, headers=headers, data=payload)
print(response.text)
