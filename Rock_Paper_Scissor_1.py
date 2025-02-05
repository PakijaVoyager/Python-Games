from random import randint

hands = ["rock","paper","scissor"]
hands1 = ["rock","paper","scissor","q"]
count = 0
computer_won = 0
while True:
    ask_usr = input("Enter rock paper scissor to play and q to quit : ").lower()
    generate = randint(0,2)
    computer = hands[generate]
    print("Computer choose : ",computer)
    if (computer == "rock") and (ask_usr == "paper"):
        print("You won")
        count+=1

    elif ask_usr not in hands1:
        print(f"{ask_usr} not in the option")
        continue

    elif (computer == "scissor") and (ask_usr == "rock"):
        print("You won")
        count+=1

    elif (computer == "paper") and (ask_usr == "scissor"):
        print("You won")
        count+=1

    elif (ask_usr == "q"):
        break

    elif (ask_usr == computer):
        print("You both choose same option :) ")
        continue

    else:
        print("You lose")
        computer_won+=1

print(f"You won {count} times")
print(f"Computer won {computer_won} times")