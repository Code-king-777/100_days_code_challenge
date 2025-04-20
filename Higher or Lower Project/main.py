#todo1: take input from user
import random
from art import logo,vs
from game_data import data

#todo2: select random people from dictionary
count1=0
count2=0
# print(game_follower_count)
# print(random_dict)
def player_a():
    random_dict1 = random.choice(data)
    global count1
    game_name=random_dict1["name"]
    game_description=random_dict1["description"]
    game_country=random_dict1["country"]
    print(f"Compair A : {game_name},a {game_description},from {game_country}")
    count1 = int(random_dict1["follower_count"])
    return count1


def player_b():
    random_dict2 = random.choice(data)
    global count2
    game_name = random_dict2["name"]
    game_description = random_dict2["description"]
    game_country = random_dict2["country"]
    print(f"Against B: {game_name},a {game_description},from {game_country}")
    count2 = int(random_dict2["follower_count"])
    return count2

score = 0
sam=True
while sam:
    print(logo)
    player_a()
    print(vs)
    player_b()
    user_choice = input("who has more follower. type 'A' or 'B' :  ").lower()

    if user_choice == "A":
        if count1 > count2:
            score += 1
            print(f"your current score is {score}.")
        else:
            print(f"you loose.your total score is {score}.")
            sam = False

    if user_choice == "B":
        if count2 > count1:
            score += 1
            print(f"your current score is {score}.")
        else:
            print(f"you loose.your total score is {score}.")
            sam = False
#todo3: compair them

# def compair():


#todo4: calculate the score
#todo5: make option b, option a next time
