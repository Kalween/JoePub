import art

game_on = True
def plus(n1,n2):
    return n1+n2
def minus(n1,n2):
    return n1-n2
def gånger(n1,n2):
    return n1*n2
def delat(n1,n2):
    return n1//n2

print(art.logo)
utfall = 0 
while game_on is True:

    if utfall == 0:
        print(utfall)
        n1 = int(input("Input number: "))
        func = input(" + , - , / , * , clear , quit: ")
        n2 = int(input("Input number: "))
        if func == '+':
            #plus(n1,n2)
            utfall = plus(n1,n2)
        elif func == '-':
            utfall = minus(n1,n2)
        elif func == '*':
            utfall = gånger(n1,n2)
        elif func == '/':
            utfall = delat(n1,n2)
        elif func == 'clear':
            n1 = 0  
            n2 = 0 
        elif func == 'quit':
            game_on = False      
    else:
        print(utfall)
        func = input(" + , - , / , * , clear , quit: ")
        if func == '+':
            n2 = int(input("Input number: "))    
            #plus(n1,n2)
            utfall = plus(utfall,n2)
        elif func == '-':
            n2 = int(input("Input number: "))
            utfall = minus(utfall,n2)
        elif func == '*':
            n2 = int(input("Input number: "))
            utfall = gånger(utfall,n2)
        elif func == '/':
            n2 = int(input("Input number: "))
            utfall = delat(utfall,n2)
        elif func == 'clear':
            utfall = 0
            n1 = 0  
            n2 = 0 
        elif func == 'quit':
            game_on = False          