import art, game_data
import random
import os

game_on = True
score = 0
print(art.logo)

def get_data():
    random_dict = random.choice(game_data.data)
    name = random_dict['name']
    follower = random_dict['follower_count']
    description = random_dict['description']
    country = random_dict['country']
    return name, follower , description , country

def check_answer(question):
    if question == 'A' and numberone[1] > numbertwo[1]:
        return score +1
    elif question == 'A' and numberone[1] < numbertwo[1]:
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(art.logo)
        print(f"Wrong, you final score was {score}")
        quit()
    elif question == 'B' and numbertwo[1] > numberone[1]:
        return score +1
    else: 
        os.system('cls' if os.name == 'nt' else 'clear') 
        print(art.logo)
        print(f"Wrong, you final score was {score}")
        quit()


while game_on == True:
    numberone = get_data()
    numbertwo = get_data()
    if numberone == numbertwo:
        numbertwo = get_data()
    print(f"Compare A: {numberone[0]}, a {numberone[2]}, from {numberone[3]}")
    print(art.vs)
    print(f"Compare B: {numbertwo[0]}, a {numbertwo[2]}, from {numbertwo[3]}")
    question = input("Who has more followers? Type 'A' or 'B': ")
    check_answer(question)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(art.logo)
    score += 1
    print(f"Correct! Curent score: {score}") 

