import random
from art import logo
def number_choice():
    number=[]
    for num in range(1,101):
        number.append(num)
    random_number=int(random.choice(number))
    return  random_number

number1=number_choice()
user_choice = 0


def check_number():
    global number1
    global user_choice
    user_choice = int(input("make a guess:"))

    if  user_choice == number1:
        print("you guess the number....congrats!")

    elif user_choice > number1:
        print("Too high...")
    elif user_choice < number1:
        print("Too low...")


def easy_level():
    a=10
    global user_choice
    while a>0 and user_choice != number1:
        print(f"you have {a} attempt remaining to guess the number... ")
        check_number()
        a-=1

def hard_level():
    a=5
    global user_choice
    while a>0 and user_choice != number1:
        print(f"you have {a} attempt remaining to guess the number... ")
        check_number()
        a -= 1


sam=True
while sam:
    print(logo)
    print("welcome to number guessing game...\nI'm thinking a number between 1 and 100 ")
    want_to_play=input("Do you want to play a number guessing game...type 'Y' or 'N' : ").lower()
    if want_to_play=="y":
        easy_or_hard = input("please select the level.....'hard' or 'easy': ").lower()

        if easy_or_hard=="easy":
            easy_level()
        elif easy_or_hard=="hard":
            hard_level()
    else:
        sam=False
    if user_choice==number1:
        sam=False
