# with open("my_file.txt", mode='r') as file:
#     content = file.read()
#     print(content)

# with open("my_file.txt", mode="w") as file:
#     file.write("\nTest new test")
import os


LETTER = "Input/Letters/starting_letter.txt"
NAMES = "Input/Names/invited_names.txt"
OUTPUT = "Output/ReadyToSend/"

with open(NAMES) as names:
    read_names = names.read()
    n = list(read_names.split("\n"))


with open(LETTER) as letter:
    content = letter.read()
    for i in n:
        x = content.replace("[name]", i)
        with open(f"{OUTPUT}{i}.txt", mode="w") as new_file:
            new_file.write(x)
#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp