import requests
import json
import sys

num = 0

topic = input(str("What do you want to learn about - people, films, starships, vehicles, species, or planets? "))

topics = ["people", "films", "starships", "vehicles", "species", "planets"]

if topic == "people":
	num = 84

if topic == "films":
	num = 7

if topic == "starships":
	num = 42

if topic == "vehicles":
	num = 74

if topic == "species":
	num = 38

if topic == "planets":
	num = 61

infoList = []


for i in range(0, num):
	i=str(i)
	url = "https://swapi.dev/api/"+topic+"/"+i+"/"
	response = requests.get(url)
	response_json = json.loads(response.text)
	infoList.append(response_json)
	print(i)




askTopic = input("What "+topic+" to you want to learn about? ")


specificTopicList = []

for j in range(1, num):
	try:
		if askTopic == infoList[j]['name']:
			print("This character is in the database")
			print(str(j))
			specificTopic = infoList[int(j)]
	except:
		print("")

print(specificTopic)



for d in specificTopic:
	n = d.replace("_"," ")
	print(n)

descriptor = input("What do you want to know about "+specificTopic['name']+" out of all the descriptors above? ")

descriptor = descriptor.replace("'"," ")


if descriptor == "name":
	print(specificTopic['name']+"'s "+descriptor+" is "+specificTopic[descriptor]+", DUH!")	
else:
	print(str(specificTopic['name'])+"'s "+descriptor+" is "+str(specificTopic[descriptor]))

