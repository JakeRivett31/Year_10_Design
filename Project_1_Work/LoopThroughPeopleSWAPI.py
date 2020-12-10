import requests
import json

url = "https://swapi.dev/api/people/1/"
response = requests.get(url)
response_json = response.json()
characterList = []



for i in range(0, 84):
	i=str(i)
	url = "https://swapi.dev/api/people/"+i+"/"
	response = requests.get(url)
	response_json = response.json()
	characterList.append(response_json)

print(characterList)