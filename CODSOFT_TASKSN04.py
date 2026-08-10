import random
options=["rock","paper","scissors"]
while True:
    user_choice=input("choose rock,paper or scissors:").lower()
    computer_choice=random.choice(options)
    print("You choose:",user_choice)
    print("computer chose:",computer_choice)
    if user_choice==computer_choice:
        print("It's a tie!")
    elif user_choice=="rock" and computer_choice=="scissors":
        print("You win!")
    elif user_choice=="paper" and computer_choice=="rock":
        print("You win!")
    elif user_choice=="scissors"and computer_choice=="paper":
        print("You win!")
    else:
        print("computer wins!")
    again=input("play again?(yes/no):")
    if again!="yes":
        print("Goodbye!")
        break
