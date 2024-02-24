import string

alphabet_list = list(string.ascii_lowercase)
#print(alphabet_list.index("g"))
def encrypt(text,shift):
    pass

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
