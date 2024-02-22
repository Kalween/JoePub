import random
word_list = ['bee','tennis']


chosen_word = random.choice(word_list)
print(f"pst the chosen word is {chosen_word}")
#TODO 1 Create an empty list called display.  # for each letter in the chosen_word, add a "_" to the diplay.


guess = input("Make a guess : ").lower()

#TODO 2 Lop through each positiuon in the chosen_word: # if the letter at that position matches 'guess' then revel that letter in the display at that position. 


for letter in chosen_word:
    if letter == guess:
        print("yes!")
    else:
        print("no")

#TODO 3 Print 'display' and you should see the guessed letter in the correct positon and every other letter replace with"_".