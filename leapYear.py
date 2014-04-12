def divisibleByFour(year):
    if year % 4 == 0:
        return True

def divisibleByHundred(year):
    if year % 100 == 0:
        return False
    else:
        return True

def divisibleByFourHundred(year):
    if year % 400 == 0:
        return True

def printer(year):
    if (divisibleByFour(year) and divisibleByHundred(year)) or divisibleByFourHundred(year):
        print ('Yup, Leap Year')
    else:
        print ('Nope, not that one')

while (True):
    year = input('Give me a year, I\'ll tell you if it\'s a Leap Year!')
    printer(year)



        
