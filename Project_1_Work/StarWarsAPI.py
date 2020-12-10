import requests
import json

url = "https://swapi.dev/api/people/1/"
response = requests.get(url)

characterList = []

for i in range(0, 84):
	i=str(i)
	url = "https://swapi.dev/api/people/"+i+"/"
	response = requests.get(url)
	response_json = response.json()
	characterList.append(str(response_json))
print(characterList)	

response_python = json.loads(response.text)

askCharacter = input("What character to you want to learn about? ")


for i in range(0, 84):
	url = "https://swapi.dev/api/people/"+str(i)+"/"
	response = requests.get(url)
	response_json = response.json()
	if askCharacter == characterList[name][i]:
		print("This character is in the database")
	else: 
		print("This character is not in the database")
	break



for d in response_json:
	n = d.replace("_"," ")
	print(n)


descriptor = input("What do you want to know about "+response_json['name']+" out of all the descriptors above? ")

descriptor = descriptor.replace("'"," ")

if descriptor == "name":
	print(response_json['name']+"'s "+descriptor+" is "+response_json[descriptor]+", DUH!")	
else:
	print(response_json['name']+"'s "+descriptor+" is "+response_json[descriptor])


