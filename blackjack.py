blackjack=''' _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
                       _/ |                
                      |__/                 
'''
print(blackjack)

import random

def deal_card():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card
user_cards=[]
computer_cards=[]
is_game_over=False

for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())    

def calc_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score,computer_score):
    if user_score==computer_score:
        return"DRAW!!"
    elif computer_score==0:
        return"YOU LOSE!! OPPONENT HAS A BLACKJACK"    
    elif user_score==0:
        return "YOU WIN!! WITH A BLACKJACK"
    elif user_score>21:
        return"YOU WENT ABOVE 21,YOU LOSE!!"
    elif computer_score>21:
        return"COMPUTER WENT ABOVE 21,YOU WIN!!"
    elif user_score>computer_score:
        return"YOU WIN!!"
    else:
        return"YOU LOSE!!"            

while not is_game_over:
    user_score=calc_score(user_cards)
    computer_score=calc_score(computer_cards)
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}, current score: {computer_score}")
    if user_score==0 or computer_score==0 or user_score>21:
        is_game_over=True
    else:
        user_deal=input("Type 'y' to get another card,type 'n' to pass: ").lower()
    if user_deal=="y":
        user_cards.append(deal_card())
    else:
        is_game_over=True    
while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calc_score(computer_cards) 
print(f"Your final hand is {user_cards} and final score was {user_score}")
print(f"Computer's final hand is {computer_cards}")
print(compare(user_score,computer_score))
