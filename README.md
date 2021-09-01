# Umbrella Enforcement and Management demos 
 
1. This python script (umbrella-enforcement.py) shows the existing entries
  in the Integration Enforcement API configuration and adds one more, just for   
  demonstration.   
  Please update the based on the enforcement API doc:  
  https://docs.umbrella.com/enforcement-api-old/reference#introduction
  Customer authentication to the API is handled by a fixed UUID-v4 Customer key.   
  Keys must be supplied with each request to the API. For example,   
  https://s-platform.api.opendns.com/1.0/events?&customerKey=1111-2222-3333-4444  
  To retrieve your key:  
  Navigate to Policies > Policy Components > Integrations.  
  Expand the appropriate integration or click Add to generate a custom Integration.

2. The second script (umb-enf-domains.py) shows how to configure domains using Management API.
