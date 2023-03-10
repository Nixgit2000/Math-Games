import random
import time
count = {'Counter': 0}

def WelcomeMessage():
    print("\033[1;32;40m   \n")
    print('Welcome to the Math Dojo!')
    time.sleep(1)
    print('Practice daily for best results.\n')
    time.sleep(1)
    print('Level 1: Multiply numbers between 1 and 10.')

def MathDojo():
    R1 = random.randint(1,10)
    R2 = random.randint(1,10)
    print('What is ',R1,' x ',R2,'?')
    Ans = int(input('>>> '))
    if Ans == R1 * R2:
        print('Good.')
        count['Counter'] += 1
        if count['Counter'] == 5:
            print('Enough! Proceed to level 2.\n')
            time.sleep(1)
            print('\nOut of nowhere the questions kept coming... Dojo style.\n')
            print('Multiply numbers between 5 and 12.')
            MathDojoLv2()
        if count['Counter'] < 5:
            if count['Counter'] == 1:
                print('You have gotten ',count['Counter'],' answer correct.')
            if count['Counter'] > 1:
                print('You have gotten ',count['Counter'],' answers correct.')
            print('Again!\n')
            MathDojo()
    else:
        print('Incorrect.\n')
        print('Your final score: ',count['Counter'])
        exit()
        MathDojo()

def MathDojoLv2():
    R1 = random.randint(5,12)
    R2 = random.randint(5,12)
    print('What is ',R1,' x ',R2,'?')
    Ans = int(input('>>> '))
    if Ans == R1 * R2:
        print('Good.')
        count['Counter'] += 1
        if count['Counter'] == 10:
            print('\nEnough! Proceed to level 3.\n')
            time.sleep(1)
            print('\nOut of nowhere the questions kept coming... Dojo style.\n')
            print('Multiply numbers between 7 and 13.')
            time.sleep(1)
            print('Welcome to Level 3.')
            MathDojoLv3()
        if count['Counter'] < 10:
            print(count)
            print('Again!\n')
            MathDojoLv2()
    else:
        print('Incorrect. You have lost.\n')
        print('Your final score: ',count['Counter'])
        exit()
        MathDojoLv2()

def MathDojoLv3():
    R1 = random.randint(7,13)
    R2 = random.randint(7,13)
    print('What is ',R1,' x ',R2,'?')
    Ans = int(input('>>> '))
    if Ans == R1 * R2:
        print('Good.')
        count['Counter'] += 1
        if count['Counter'] == 15:
            print('\nEnough! Proceed to level 4.\n')
            time.sleep(1)
            print('\nOut of nowhere the questions kept coming... Dojo style.\n')
            print('Multiply numbers between 10 and 20.')
            MathDojoLv4()
        if count['Counter'] < 15:
            print(count)
            print('Again!\n')
            MathDojoLv3()
    else:
        print('Incorrect. You have lost.\n')
        print('Your final score: ',count['Counter'])
        exit()
        MathDojoLv3()

def MathDojoLv4():
    R1 = random.randint(10,20)
    R2 = random.randint(10,20)
    print('What is ',R1,' x ',R2,'?')
    Ans = int(input('>>> '))
    if Ans == R1 * R2:
        print('Good.')
        count['Counter'] += 1
        if count['Counter'] == 20:
            print('\nEnough! Proceed to level 5.\n')
            time.sleep(1)
            print('\nOut of nowhere the questions kept coming... Dojo style.\n')
            print('Welcome to Level 5.')
            print('Multiply numbers between 20 and 30.')
            MathDojoLv5()
        if count['Counter'] < 20:
            print(count)
            print('Again!\n')
            MathDojoLv4()
    else:
        print('Incorrect. You have lost.\n')
        print('Your final score: ',count['Counter'])
        exit()
        MathDojoLv4()

def MathDojoLv5():
    R1 = random.randint(20,30)
    R2 = random.randint(20,30)
    print('What is ',R1,' x ',R2,'?')
    Ans = int(input('>>> '))
    if Ans == R1 * R2:
        print('Good.')
        count['Counter'] += 1
        if count['Counter'] == 25:
            print('\nEnough! Proceed to level 6.\n')
            time.sleep(1)

            print('\nOut of nowhere the questions kept coming... Dojo style.\n')
            print('Welcome to Level 6.')
            print('Multiply numbers between 30 and 40.')
            MathDojoLv6()
        if count['Counter'] < 25:
            print(count)
            print('Again!\n')
            MathDojoLv5()
    else:
        print('Incorrect. You have lost.\n')
        print('Your final score: ',count['Counter'])
        exit()
        MathDojoLv5()

def MathDojoLv6():
    R1 = random.randint(30,40)
    R2 = random.randint(30,40)
    print('What is ',R1,' x ',R2,'?')
    Ans = int(input('>>> '))
    if Ans == R1 * R2:
        print('Good.')
        count['Counter'] += 1
        if count['Counter'] == 30:
            print('\nEnough! Proceed to level 7.\n')
            time.sleep(1)

            print('\nOut of nowhere the questions kept coming... Dojo style.\n')
            print('Welcome to Level 7.')
            print('Multiply numbers between 40 and 50.')
            MathDojoLv6()
        if count['Counter'] < 30:
            print(count)
            print('Again!\n')
            MathDojoLv6()
    else:
        print('Incorrect. You have lost.\n')
        print('Your final score: ',count['Counter'])
        exit()
        MathDojoLv6()

def MathDojoLv7():
    R1 = random.randint(40,50)
    R2 = random.randint(40,50)
    print('What is ',R1,' x ',R2,'?')
    Ans = int(input('>>> '))
    if Ans == R1 * R2:
        print('Good.')
        count['Counter'] += 1
        if count['Counter'] == 35:
            time.sleep(1)

            print('\nOut of nowhere the questions kept coming... Dojo style.\n')
            print('Welcome to Level 8.')
            print('Multiply numbers between 50 and 60.')
            MathDojoLv7()
        if count['Counter'] < 35:
            print(count)
            print('Again!\n')
            MathDojoLv7()
    else:
        print('Incorrect. You have lost.\n')
        print('Your final score: ',count['Counter'])
        exit()
        MathDojoLv7()

def MathDojoLv8():
    R1 = random.randint(50,60)
    R2 = random.randint(50,60)
    print('What is ',R1,' x ',R2,'?')
    Ans = int(input('>>> '))
    if Ans == R1 * R2:
        print('Good.')
        count['Counter'] += 1
        if count['Counter'] == 40:
            print('\nEnough! Proceed to level 9.\n')
            time.sleep(1)

            print('\nOut of nowhere the questions kept coming... Dojo style.\n')
            print('Welcome to Level 9.')
            print('Multiply numbers between 60 and 70.')
            MathDojoLv8()
        if count['Counter'] < 40:
            print(count)
            print('Again!\n')
            MathDojoLv8()
    else:
        print('Incorrect. You have lost.\n')
        print('Your final score: ',count['Counter'])
        exit()
        MathDojoLv8()


def MathDojoLv9():
    R1 = random.randint(60,70)
    R2 = random.randint(60,70)
    print('What is ',R1,' x ',R2,'?')
    Ans = int(input('>>> '))
    if Ans == R1 * R2:
        print('Good.')
        count['Counter'] += 1
        if count['Counter'] == 45:
            print('\nEnough! Proceed to level 10.\n')
            time.sleep(1)

            print('\nOut of nowhere the questions kept coming... Dojo style.\n')
            print('Welcome to Level 10.')
            print('Multiply numbers between 70 and 80.')
            MathDojoLv10()
        if count['Counter'] < 45:
            print(count)
            print('Again!\n')
            MathDojoLv9()
    else:
        print('Incorrect. You have lost.\n')
        print('Your final score: ',count['Counter'])
        exit()
        MathDojoLv9()

def MathDojoLv10():
    R1 = random.randint(70,80)
    R2 = random.randint(70,80)
    print('What is ',R1,' x ',R2,'?')
    Ans = int(input('>>> '))
    if Ans == R1 * R2:
        print('Good.')
        count['Counter'] += 1
        if count['Counter'] == 50:
            print('\nEnough! Proceed to level 11.\n')
            time.sleep(1)

            print('\nOut of nowhere the questions kept coming... Dojo style.\n')
            print('Welcome to Level 11.')
            print('Multiply numbers between 80 and 90.')
            MathDojoLv11()
        if count['Counter'] < 50:
            print(count)
            print('Again!\n')
            MathDojoLv10()
    else:
        print('Incorrect. You have lost.\n')
        print('Your final score: ',count['Counter'])
        exit()
        MathDojoLv10()

def MathDojoLv11():
    R1 = random.randint(80,90)
    R2 = random.randint(80,90)
    print('What is ',R1,' x ',R2,'?')
    Ans = int(input('>>> '))
    if Ans == R1 * R2:
        print('Good.')
        count['Counter'] += 1
        if count['Counter'] == 55:
            print('\nEnough! Proceed to level 12.\n')
            time.sleep(1)

            print('\nOut of nowhere the questions kept coming... Dojo style.\n')
            print('Welcome to Level 12.')
            print('Multiply numbers between 90 and 100.')
            MathDojoLv12()
        if count['Counter'] < 55:
            print(count)
            print('Again!\n')
            MathDojoLv11()
    else:
        print('Incorrect. You have lost.\n')
        print('Your final score: ',count['Counter'])
        exit()
        MathDojoLv11()


def MathDojoLv12():
    R1 = random.randint(90,100)
    R2 = random.randint(90,100)
    print('A final door has opened. It leads you into the quantum realm where body, space and time have merged. You have almost ascended.')
    print('What is ',R1,' x ',R2,'?')
    Ans = int(input('>>> '))
    if Ans == R1 * R2:
        print('Good.')
        count['Counter'] += 1
        if count['Counter'] == 60:
            print('\nEnough! The quantum realm closes and time reverses to yesterday. See you tomorrow.')
            time.sleep(2)
            print('Come prepared.')
        if count['Counter'] < 60:
            print(count)
            print('Again!\n')
            MathDojoLv12()
    else:
        print('Incorrect. You have lost.\n')
        print('Your final score: ',count['Counter'])
        exit()
        MathDojoLv12()




WelcomeMessage()
MathDojo()

