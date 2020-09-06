a = 1
b = 10
c = 12
d = 3
Even_sum = 0
Odd_sum = 0
print ('Expected output:')
if a % 2 == 0:
    Even_sum += a
else:
    Odd_sum += a
if b % 2 == 0:
    Even_sum += b
else:
    Odd_sum += b
if c % 2 == 0:
    Even_sum += c
else:
    Odd_sum += c
if d % 2 == 0:
    Even_sum += d
else:
    Odd_sum += d

print ('Even sum:', Even_sum)
print ('Odd sum:', Odd_sum)
