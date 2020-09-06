name = input('What is your name: ')
print('hello, ' ,name)
print('MAC Lipstick $18')
print('MAC Foundation $35')

total = 0

product = input('What do you want to buy: ')
if product == 'lipstick':
    total = total + 18
    print('$18')
elif product == 'foundation':
    print('$35')
    total = total + 35
else:
    print('None available')

is_continued = input('Press y if you want to keep buying or any other characters to exit: ')

while is_continued == 'y':
    product2 = input('What else do you want to buy: ')
    if product2 == 'lipstick':
        total += 18
        print('$18')
    elif product2 == 'foundation':
        total += 35
        print('$35')
    else:
        print('None availabe')
    is_continued = input('Press y if you want to keep buying or any other characters to exit: ')


print('Your total is', total)
