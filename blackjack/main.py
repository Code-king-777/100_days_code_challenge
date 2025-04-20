import random
from art import logo
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# want_to_play = input("Do you want to play a game of blackjack? type 'y' or 'n' : ").lower()

black_jack=21

user_choice=random.sample(cards,2)
print(f"your cards: {user_choice}, current score : {user_choice[0]+user_choice[1]}")
user_score=user_choice[0]+user_choice[1]
dealer_choice=random.sample(cards,2)
print(f"Dealer's first card:{dealer_choice[0]}")
dealer_score=dealer_choice[0]+dealer_choice[1]

if user_score==black_jack or dealer_score==black_jack:
    if user_score==black_jack:
        print(f"you got {black_jack}(BLACKJACK) you win...")
    if dealer_score==black_jack:
        print(f"Dealer got {black_jack}(BLACKJACK) you loose...")

if user_score > black_jack:
    if user_choice[0]  and user_choice[1] == 11:
        user_choice[0]=1
        user_choice[1]=1
    elif user_choice[0]==11:
        user_choice[0]=1
    elif user_choice[1]==11:
        user_choice[1]=1
    else:
        print("you loose....")

sam=True
if user_score or dealer_score != black_jack:
    while sam:
        want_another_card = input("Do you want another card or pass....press 'y' or 'n'.. ").lower()

        if user_score < black_jack:
            if want_another_card=="y":
                draw_another_card=random.choice(cards)
                user_choice.append(draw_another_card)
                user_score+=draw_another_card
                print(f"your cards: {user_choice}, current score : {user_score}")

        if want_another_card >= "n":
            # print(f"your cards: {user_choice}, current score : {user_score}")
            sam=False

