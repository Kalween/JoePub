import random

game_on = True
EASY = 10
HARD = 5

def difficulty():
    game_mode = input("Choose Easy or Hard : ")
    if game_mode == 'easy':
        return EASY
    else:
        return HARD


def check_answer(attempt, number):
    if attempt == number:
        print("You win!")
        quit()
    elif attempt > number:
        print("Lower")
    elif attempt < number:
        print("Higher")



number = random.randint(1,100)

turns = difficulty()
while turns > 0 or attempt != number:
    print(f"You have {turns} numbers of turns to guess")
    attempt = int(input("Guess the number: "))
    check_answer(attempt, number)
    turns -= 1
