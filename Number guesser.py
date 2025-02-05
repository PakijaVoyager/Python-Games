from random import randint

count = 0
ask_usr = 0
guess = randint(1,10)
while guess != ask_usr:
    ask_usr = int(input("Guess the number : "))
    if ask_usr > guess:
        print("You are above the number")
        count+=1
    elif ask_usr < guess:
        print("You are below the number")
        count+=1
print("You get it in",count,"times")
