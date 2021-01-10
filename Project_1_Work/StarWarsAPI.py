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


specificCharacterList = []

for j in range(1, 84):
	try:
		if askCharacter == characterList[j]['name']:
			print("This character is in the database")
			print(str(j))
			specificCharacter = characterList[int(j)]
	except:
		print("")


print(specificCharacter)

for d in specificCharacter:
	n = d.replace("_"," ")
	print(n)


descriptor = input("What do you want to know about "+specificCharacter['name']+" out of all the descriptors above? ")

descriptor = descriptor.replace("'"," ")

if descriptor == "name":
	print(specificCharacter['name']+"'s "+descriptor+" is "+specificCharacter[descriptor]+", DUH!")	
else:
	print(str(specificCharacter['name'])+"'s "+descriptor+" is "+str(specificCharacter[descriptor]))