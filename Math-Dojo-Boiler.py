import time
import random
Count = {'Counter': 0}

def Welcome():
    print('Welcome to the Math Dojo: Boiler Edition!')
    print('Level 1')

def MathDojo():
    a = 1+Count['Counter']
    b = 10+Count['Counter']
    c = 1+Count['Counter']
    d = 10+Count['Counter']
    A = random.randint(a,b)
    B = random.randint(c,d)
    print('What is ',A,' x ',B)
    Ans = int(input('>>> '))
    if Ans == A*B:
        Count['Counter'] += 1
        print(Count['Counter'])
        print('Good. Again!')
        MathDojo()
    if Ans != A*B:
        print('Good try, but incorrect. Play again.')
        print('Your score: ',Count['Counter'])
        exit()

Welcome()
MathDojo()


