# with open("my_file.txt", mode='r') as file:
#     content = file.read()
#     print(content)

# with open("my_file.txt", mode="w") as file:
#     file.write("\nTest new test")
import os


LETTER = "Input/Letters/starting_letter.txt"
NAMES = "Input/Names/invited_names.txt"

with open(LETTER) as letter:
    content = letter.read()
    print(content)
    for i in content:
        print(i)
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp