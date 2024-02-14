import data
from random import random

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

# new_question = Question("Are you dum dum", "True")
# print(new_question.text)
# user = input(print(f"{new_question.text} (True or False): "))
# if user == new_question.answer:
#     print("bravo")
        
# for item in data.question_data:
#     print(item)