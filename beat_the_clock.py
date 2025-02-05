import time
from random import choice,randint
import threading

num_question = int(input("Enter the number of question to ask : "))
time_ = int(input("Enter the time in seconds as timer : "))
operators = ["+","-","*"]
time_up = False

# This function change the value of time_up variable if the time reaches.
def timer_():
    global time_up
    time_up = False
    time.sleep(time_)
    time_up = True
    print("Time's up!")

# This function generates the questions of random number from 3 to 15 and return's it.
def generate():
    f1 = randint(3,15)
    f2 = randint(3,15)
    choose_operator = choice(operators)
    question = str(f1) + " " + choose_operator + " " + str(f2)
    return question

# This is the main function that gets the question and also checks for the answer and simultaneously checks for the timer and stops the program if time's up.
def initiator():
    count = 0
    check = threading.Thread(target=timer_,daemon=True) #threading module is used for checking the time
    check.start()
    for i in range(num_question):
        question = generate()
        answer = eval(question)
        if question == answer:
            count+=1
    print(f"You answered {count} questions")

if __name__ == "__main__":
    initiator()