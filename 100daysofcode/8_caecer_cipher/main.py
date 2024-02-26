import string

alphabet_list = list(string.ascii_lowercase)
#print(alphabet_list.index("g"))
shifted_list = []

def encrypt(text,shift):
    for i in text:
        if i == " ":
           shifted_list.append(" ")

        elif  alphabet_list.index(i)+shift > 25:
            shift_value = alphabet_list.index(i)+shift -25 
        else:
            shift_value = alphabet_list.index(i)+shift
            shifted_list.append(alphabet_list[shift_value])
    print("".join(shifted_list))

def decrypt(text, shift):
    shifted_list = []
    for i in text:
        if i == " ":
            shifted_list.append(" ")
        elif alphabet_list.index(i) - shift < 0:
            shift_value = alphabet_list.index(i) - shift + 26
        else:
            shift_value = alphabet_list.index(i) - shift
            shifted_list.append(alphabet_list[shift_value])
    print("".join(shifted_list))

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
game_on = True
print("welcome to ceacer cipher.")
while game_on == True:
    choice = input("Would you like to encrypt or decrypt?: ")
    if choice == "encrypt":        
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        encrypt(text,shift)
    elif choice == "decrypt":
        text = input("Type your d message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        decrypt(text,shift)
    elif choice == "q":
        quit()
    else:
        print("Wrong input, try again.")
