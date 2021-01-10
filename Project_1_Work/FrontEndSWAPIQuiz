import requests
import json
import random


topics = ["people", "starships", "vehicles", "species", "planets"]

randTopicIndex = random.randint(0, 5)

randTopic = topics[randTopicIndex]

infoList = []

num = 0

chosenTopicAttributeList = []

if randTopic == "people":
     num = 84

if randTopic == "films":
     num = 7

if randTopic == "starships":
     num = 42

if randTopic == "vehicles":
     num = 74

if randTopic == "species":
     num = 38

if randTopic == "planets":
     num = 61

print(randTopic)

for i in range(1, num):
     i=str(i)
     url = "https://swapi.dev/api/"+randTopic+"/"+i+"/"
     response = requests.get(url)
     response_json = json.loads(response.text)
     infoList.append(response_json)
     print(i)



chosenTopicRandInt = random.randint(2, num-1)
chosenTopic = infoList[chosenTopicRandInt]  

randTopicInt1 = random.randint(2, num-1)
randTopic1 = infoList[randTopicInt1]

randTopicInt2 = random.randint(2, num-1)
randTopic2 = infoList[randTopicInt2]

randTopicInt3 = random.randint(2, num-1)
randTopic3 = infoList[randTopicInt3]



for d in chosenTopic:
     chosenTopicAttributeList.append(d)

print(chosenTopicAttributeList)     


chosenTopicAttributeListRandInt = random.randint(0, len(chosenTopicAttributeList)-5)

chosenTopicAttribute = chosenTopicAttributeList[chosenTopicAttributeListRandInt]

print(chosenTopicAttribute)

try:
     print(chosenTopic[chosenTopicAttribute])
     print(randTopic1[chosenTopicAttribute])
     print(randTopic2[chosenTopicAttribute])
     print(randTopic3[chosenTopicAttribute])
except:
     print("")


class Question:
     def __init__(self, prompt, answer):
          self.prompt = prompt
          self.answer = answer

question_prompts = [
     "What is "+str(chosenTopic["name"])+"'s "+str(chosenTopicAttribute)+"?\n(a) "+
     str(chosenTopic[chosenTopicAttribute])+"\n(b) "+
     str(randTopic1[chosenTopicAttribute])+"\n(c) "+
     str(randTopic2[chosenTopicAttribute])+"\n",
     "What color are bananas?\n(a) Red/Green\n(b)Yellow\n",
]

questions = [
     Question(question_prompts[0], "a"),
     Question(question_prompts[1], "b"),
]

def run_quiz(questions):
     score = 0
     for question in questions:
          answer = input(question.prompt)
          if answer == question.answer:
               score += 1
     print("you got", score, "out of", len(questions))

run_quiz(questions)