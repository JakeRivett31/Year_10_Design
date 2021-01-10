import requests
import json
import random
import tkinter as tk

topics = ["people", "species", "planets"]

randTopicIndex = random.randint(0, 2)

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



chosenTopicRandInt = random.randint(2, num-2)
chosenTopic = infoList[chosenTopicRandInt]  

randTopicInt1 = random.randint(2, num-2)
randTopic1 = infoList[randTopicInt1]

randTopicInt2 = random.randint(2, num-2)
randTopic2 = infoList[randTopicInt2]

randTopicInt3 = random.randint(2, num-2)
randTopic3 = infoList[randTopicInt3]



for d in chosenTopic:
     chosenTopicAttributeList.append(d)

print(chosenTopicAttributeList)     


chosenTopicAttributeListRandInt = random.randint(0, len(chosenTopicAttributeList))

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




def popup_window():
    window = tk.Toplevel()

    label = tk.Label(window, text="Hello World!")
    label.grid(row=0, column=1)

    chosenTopicLabel = tk.Label(window, text="hi")
    label.grid(row=1, column=1)

    button_close = tk.Button(window, text="Close", command=window.destroy)
    button_close.grid(row=2, column=1)

def popup_showinfo():
    showinfo("ShowInfo", "Hello World!")

def quiz_submission():
     quiz_submission = entryBox1.get()

     if quiz_submission == "a":
          answerLabel = tk.Label(canvas1, text="Correct!")
          answerLabel.config(bg="green", fg="white")
          answerLabel.grid(row=6, column=0)
     else:
          answerLabel = tk.Label(canvas1, text="Wrong :(")
          answerLabel.config(bg="red", fg="white")
          answerLabel.grid(row=6, column=0)

def database_submission(*args):
     global database_submission
     global specificCharacter
     database_submission = entryBox2.get()
     database_submission = str(database_submission)

     characterList = []

     for i in range(0, 84):
          i=str(i)
          url = "https://swapi.dev/api/people/"+i+"/"
          response = requests.get(url)
          response_json = json.loads(response.text)
          characterList.append(response_json)
          print(i)

     for j in range(1, 84):
          try:
               if database_submission == characterList[j]['name']:
                    print("This character is in the database")
                    print(str(j))
                    specificCharacter = characterList[int(j)]
                    print(specificCharacter)
          except:
               print("")
     

     heightLabel = tk.Label(canvas2, text="Height (cm) - "+specificCharacter["height"])
     heightLabel.config(bg="black", fg="yellow")
     heightLabel.grid(row=6, column=1)

     massLabel = tk.Label(canvas2, text="Mass (kg) - "+specificCharacter["mass"])
     massLabel.config(bg="black", fg="yellow")
     massLabel.grid(row=7, column=1)

     hairLabel = tk.Label(canvas2, text="Hair Colour - "+specificCharacter["hair_color"])
     hairLabel.config(bg="black", fg="yellow")
     hairLabel.grid(row=8, column=1)

     skinLabel = tk.Label(canvas2, text="Skin Colour - "+specificCharacter["skin_color"])
     skinLabel.config(bg="black", fg="yellow")
     skinLabel.grid(row=9, column=1)

     eyeLabel = tk.Label(canvas2, text="Eye Colour - "+specificCharacter["eye_color"])
     eyeLabel.config(bg="black", fg="yellow")
     eyeLabel.grid(row=10, column=1)

     birthYearLabel = tk.Label(canvas2, text="Birth Year - "+specificCharacter["birth_year"])
     birthYearLabel.config(bg="black", fg="yellow")
     birthYearLabel.grid(row=11, column=1)

     genderLabel = tk.Label(canvas2, text="Gender - "+specificCharacter["gender"])
     genderLabel.config(bg="black", fg="yellow")
     genderLabel.grid(row=12, column=1)



print("Start Program")

root = tk.Tk()



root.config(bg="black")

title = tk.Label(root, text = "Star Wars Quiz and Database")
#Configuration
title.config(font =("News Gothic", "50"), fg = "yellow", bg = "black")

title.grid(row=0, column=0, columnspan=2)


button_close = tk.Button(root, text="Close", command=root.destroy)
button_close.grid(row=13, column=0, columnspan=2)

canvas1 = tk.Canvas(root, bg="black", height=5000, width=5000)
canvas1.grid(row=1, column=0)

canvas1Title = tk.Label(canvas1, fg="yellow", bg="black", text="STAR WARS QUIZ")
canvas1Title.grid(row=2, column=0)

questionLabel = tk.Label(canvas1, text=question_prompts[0])
questionLabel.grid(row=3, column=0)

name_var = tk.StringVar()

entryBox1 = tk.Entry(canvas1, bd =5, textvariable=name_var)
entryBox1.grid(row=4, column=0)


submitButton1 = tk.Button(canvas1, text="Submit", command=quiz_submission)
submitButton1.grid(row=5, column=0)

canvas2 = tk.Canvas(root, bg="black", height=5000, width=5000)
canvas2.grid(row=1, column=1)

canvas2Title = tk.Label(canvas2, fg="yellow", bg="black", text="Star Wars Database")
canvas2Title.grid(row=2, column=1)

topicLabel = tk.Label(canvas2, text="Which character are you interested in?")
topicLabel.grid(row=3, column=1)

entryBox2 = tk.Entry(canvas2, bd=5, textvariable=name_var)
entryBox2.grid(row=4, column=1)

submitButton2 = tk.Button(canvas2, text="Submit", command=database_submission)
submitButton2.grid(row=5, column=1)


root.mainloop()

print("End Program")