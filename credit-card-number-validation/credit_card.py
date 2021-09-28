#card_number = input('your card number: ')

# this function is to ensure the valid length of a credit card (no < 13 and no > 16 digits)
def is_valid_digit(card_number):
    if len(card_number) < 13:
        return False
    elif len(card_number) > 16:
        return False
    else:
        return True

# function reverses the the credit card numbers 
def reverse(card_number):
    reverse_s = ''
    i = len(card_number) - 1
    while i >= 0:
        reverse_s = reverse_s + card_number[i]
        i = i - 1
    return reverse_s

# test1 = '4388576018402626'
# test2 = '379354508162306'
# test3 = '2398746'
#
# print(reverse(test1))
# print(reverse(test2))
# print(reverse(test3))

def one_digit(number):
    if number > 9:
        number = int(number % 10 + number // 10)
    return number

# test = 19
# test4 = 5
# test5 = 23
# print(one_digit(test))
# print(one_digit(test4))
# print(one_digit(test5))

def even_place_digit(number):
    sum = 0
    for i in range(len(number)):
        if i % 2 != 0:
            sum += one_digit(int(number[i]) * 2)
    return sum
def odd_place_digit(number):
    sum = 0
    for i in range(len(number)):
        if i % 2 == 0:
            sum += int(number[i])
    return sum

# test6 = '245768391'
# test7 = '438938493'
# test8 = '123456789'
# print(even_place_digit(test6))
# print(even_place_digit(test7))
# print(odd_place_digit(test8))

def is_correct(card_number):
    if not is_valid_digit(card_number):
        return False
    else:
        reverse_number = reverse(card_number)
        sum = int(even_place_digit(reverse_number) + odd_place_digit(reverse_number))
        if sum % 10 == 0:
            return True
        else:
            return False

# test9 = '379354508162306'
# test10 = '4388576018402626'
# test11 = '23456'
# print(is_correct(test9))
# print(is_correct(test10))
# print(is_correct(test11))

def main():
    user_input = str(input('enter card number for testing: '))
    if is_correct(user_input):
        print('your credit card number is valid')
    else:
        print('your credit card number is invalid')

main()
