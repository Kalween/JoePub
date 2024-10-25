nato_alfabet_svenska = {
    "A": "Adam",
    "B": "Bertil",
    "C": "Caesar",
    "D": "David",
    "E": "Erik",
    "F": "Fredrik",
    "G": "Gustav",
    "H": "Helge",
    "I": "Ivar",
    "J": "Johan",
    "K": "Kalle",
    "L": "Ludvig",
    "M": "Martin",
    "N": "Niklas",
    "O": "Olof",
    "P": "Petter",
    "Q": "Qvintus",
    "R": "Rudolf",
    "S": "Sigurd",
    "T": "Tore",
    "U": "Urban",
    "V": "Viktor",
    "W": "Wilhelm",
    "X": "Xerxes",
    "Y": "Yngve",
    "Z": "Zäta",
    "Å": "Åke",
    "Ä": "Ärlig",
    "Ö": "Östen"
}


ord_input = input("Skriv ett ord: ")

bokstäver = [l.upper() for l in ord_input]
nato = [(nato_alfabet_svenska[letter]) for letter in bokstäver if letter in nato_alfabet_svenska]
print(nato)