import requests
import json
import pprint

response = requests.get("http://www.recipepuppy.com/api/")

response.json()

print(response.status_code)







