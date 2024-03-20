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
def clear(n1,n2):
    n1 = 0
    n2 = 0

beräkningar = {
    '+': plus,
    '-': minus,
    '*': gånger,
    '/': delat,
    'c': clear
}

print(art.logo)
while game_on is True:
    utfall = 0 

    if utfall == 0:
        
        n1 = int(input('First number: '))
        for symbol in beräkningar:
            print(symbol)
        symbol = input('Pick a calculation symbol from above : ')
        n2 = int(input('Second number: '))
        answer = beräkningar[f'{symbol}'](n1,n2)
    elif func == 'clear':
        n1 = 0  
        n2 = 0
        utfall == 0
        print(art.logo)
    elif func == 'quit':
        game_on = False 
    else:
        print(f'{n1} {symbol} {n2} = {answer}')
        symbol = input('Pick a calculation symbol from above : ')
        n2 = int(input(f"{symbol} number: ")) 
exit()
while game_on is True:

    if utfall == 0:
        print(utfall)
        n1 = int(input("Input first number: "))
        func = input(" + , - , / , * , clear , quit: ")
        n2 = int(input("Input second number: "))
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