import string

alphabet_list = list(string.ascii_lowercase)
#print(alphabet_list.index("g"))
shifted_list = []

def encrypt(text,shift):
    for i in text:
        shift_value = alphabet_list.index(i)+shift
        if alphabet_list.index(i)+shift > 25:
            shift_value = alphabet_list.index(i)+shift -25 
        shifted_list.append(alphabet_list[shift_value])
    print(shifted_list)

def decrypt(text,shift):
    for i in text:
        shift_value = alphabet_list.index(i)-shift
        if alphabet_list.index(i)+shift < 25:
            shift_value = alphabet_list.index(i)+shift +25 
        shifted_list.append(alphabet_list[shift_value])
    print(shifted_list)

#direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

decrypt(text,shift)