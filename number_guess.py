from random import randint
EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5

def check_answer(guess,answer,turns):
    if guess>answer:
        print("Too High")
        return turns-1
    elif guess<answer:
        print("Too Low")
        return turns-1
    else:
        print("You got it!!")

def set_difficulty():
    level=input("Choose a difficulty,Type 'easy' OR 'hard' ").lower()
    if level=='easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS    
def game():
    print("WELCOME TO THE NUMBER GUESSING GAME")
    print("I'm guessing a number between 1 to 100")
    answer=randint(1,100)
    turns=set_difficulty()
    guess=0
    while guess!=answer:
        print(f"You have {turns} attempts remaining to guess the number")
        guess=int(input("Make a guess: "))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("You Lose!!")
            print(f"The answer is {answer}")
            return
game()        