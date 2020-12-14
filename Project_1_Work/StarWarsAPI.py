import requests
import json




characterList = []

for i in range(0, 84):
	i=str(i)
	url = "https://swapi.dev/api/people/"+i+"/"
	response = requests.get(url)
	response_json = json.loads(response.text)
	characterList.append(response_json)
	print(i)


print(characterList[1]['name'])



askCharacter = input("What character to you want to learn about? ")

characterURL = ""
characterResponse = ""
characterResponse_json = ""
specificCharacterList = []

for j in range(1, 84):
	try:
		if askCharacter == characterList[j]['name']:
			print("This character is in the database")
			print(str(j))
			characterURL = "https://swapi.dev/api/people/"+j+"/"
			characterResponse = requests.get(characterURL)
			characterResponse_json = json.loads(characterResponse.text)
			specificCharacterList.append(characterResponse_json)
	except:
		print("")

print(specificCharacterList)

for d in response_json:
	n = d.replace("_"," ")
	print(n)


descriptor = input("What do you want to know about "+characterResponse_json['name']+" out of all the descriptors above? ")

descriptor = descriptor.replace("'"," ")

if descriptor == "name":
	print(response_json['name']+"'s "+descriptor+" is "+response_json[descriptor]+", DUH!")	
else:
	print(response_json['name']+"'s "+descriptor+" is "+response_json[descriptor])


