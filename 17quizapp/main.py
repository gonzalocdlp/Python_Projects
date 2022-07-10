import data

class User:

    def __init__(self, question, answer):
        self.question = question
        self.answer= answer
ison='true'
score=0
while ison=='true':
    user1=User(data.question_data[score]["text"], data.question_data[score]["answer"])
    user1answer=user1.answer
    user1question=user1.question

    answer=input(f"True or false {user1question}").capitalize()
    if answer==user1answer:
        score=score+1
        print(f"Correct! your score is {score}")
    else:
        print(f'Incorrect. game is over final score is {score}')
        ison='false'