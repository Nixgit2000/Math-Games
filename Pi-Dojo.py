import time
Pi = {'1': 3, '2': 1, '3': 4, '4': 1, '5': 5, '6': 9, '7': 2, '8': 6, '9': 5, '10': 3, '11': 5, '12': 8, '13': 9, '14': 7, '15': 9, '16': 3, '17': 2, '18': 3, '19': 8, '20': 4, '21': 6, '22': 2, '23': 6, '24': 4, '25': 3, '26': 3, '27': 8, '28': 3, '29': 2, '30': 7, '31': 9, '32': 5, '33': 0, '34': 2, '35': 8, '36': 8, '37': 4, '38': 1, '39': 9, '40': 7, '41': 1, '42': 6, '43': 9, '44': 3, '45': 9, '46': 9, '47': 3, '48': 7, '49': 5, '50': 1, '51': 0, '52': 5, '53': 8, '54': 2, '55': 0, '56': 9, '57': 7, '58': 4, '59': 9, '60': 4, '61': 4, '62': 5, '63': 9, '64': 2, '65': 3, '66': 0, '67': 7, '68': 8, '69': 1, '70': 6, '71': 4, '72': 0, '73': 6, '74': 2, '75': 8, '76': 6, '77': 2, '78': 0, '79': 8, '80': 9, '81': 9, '82': 8, '83': 6, '84': 2, '85': 8, '86': 0, '87': 3, '88': 4, '89': 8, '90': 2, '91': 5, '92': 3, '93': 4, '94': 2, '95': 1, '96': 1, '97': 7, '98': 0, '99': 6, '100': 7, '101': 9}
i = 1
print('Welcome to the Pi Dojo.\n')
time.sleep(1)
print('For best results practice daily.\n')
time.sleep(1)
print('Tip: For the list of digits, feel free to pull up 100 digits of Pi on a search engine.\n')

def Function():
    global i
    print('Value ',i)
    A = int(input('>>> '))
    if A == Pi[str(i)]:
        print('\n')
        i += 1
        Function()
    else:
        print('\nIncorrect! You got ',str(i-1),' digits of Pi correct. Try again!')
        print('The next few digits are: ',Pi[str(i)],' ',Pi[str(i+1)],' and ',Pi[str(i+2)])
        print('\n======(CTRL+SHIFT+F10 to reset)======')
time.sleep(2)
Function()
