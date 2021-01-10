topics = ["people", "species", "planets", "films", "starships", "vehicles"]

randTopicIndex = random.randint(0, 5)

randTopic = topics[randTopicIndex]

infoList = []

num = 0

chosenTopicAttributeList = []

if randTopic == "people":
     num = 82

if randTopic == "films":
     num = 6

if randTopic == "starships":
     num = 40

if randTopic == "vehicles":
     num = 72

if randTopic == "species":
     num = 37

if randTopic == "planets":
     num = 60

print(randTopic)

for i in range(1, num):
     i=str(i)
     url = "https://swapi.dev/api/"+randTopic+"/"+i+"/"
     response = requests.get(url)
     response_json = json.loads(response.text)
     infoList.append(response_json)
     print(i)