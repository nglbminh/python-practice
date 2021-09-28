import random

min = int(input ('what is your min: '))
max = int(input ('what is your max: '))

while min >= max:
    print('error, try again')
    min = int(input('what is your min: '))
    max = int(input('what is your max: '))


x = random.randint (min, max)

n = int(input('guess the mysterious number: '))

while x != n:
 if n > x:
    print('too high, try again')
    n = int(input('guess the mysterious number: '))
 elif n < x:
    print('too low, try again')
    n = int(input('guess the mysterious number: '))

print ('you got it!')
