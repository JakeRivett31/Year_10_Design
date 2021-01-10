import requests
import json
import random


randCharacterInt = random.randint(1, 83)



characterList = []

for i in range(0, 84):
	i=str(i)
	url = "https://swapi.dev/api/people/"+i+"/"
	response = requests.get(url)
	response_json = json.loads(response.text)
	characterList.append(response_json)
	print(i)


randomCharacter = characterList[randCharacterInt]

print(randomCharacter['name'])

randomCharacterAttributes = []

for d in randomCharacter:
	n = d.replace("_"," ")
	randomCharacterAttributes.append(n)

print(randomCharacterAttributes)

randomListInt = random.randint(0, 7)

randomListAttribute = randomCharacterAttributes[randomListInt]

print(randomListAttribute)
print(randomCharacter[randomListAttribute])
print(randomCharacter+"'s"+randomListAttribute+is )
