import random
import art
word_list = ['bee','tennis']


chosen_word = random.choice(word_list)
print(f"pst the chosen word is {chosen_word}")

display = []
for i in chosen_word:
    display.append("_")

print(" ".join(display))

lives = 0

while "_" in display and lives <7:

    guess = input("Make a guess : ").lower()
    for index, letter in enumerate(chosen_word):
        if letter == guess:
            display[index] = letter

    if guess not in chosen_word:
        print(art.stages[lives])
        lives +=1



    print(" ".join(display))

if lives == 7:
    print("You lost!")
else: 
    print("You won congrats!")