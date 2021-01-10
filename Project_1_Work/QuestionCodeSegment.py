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
