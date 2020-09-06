# a function to calculate sum of the even indices number in list ls
def sum_of_even_index(ls):
    sum = 0
    index = 0
    while index < len(ls):
        if index % 2 == 0:
            sum += ls[index]
        index += 1
    return sum

apple = [5,3,2,10,1,4]
print (sum_of_even_index(apple))
apple.append(1)
print(apple)
########################################
# a function named reverse add to the ls list and ouput the reverse list
def reverse(ls):
    newlist = []
    index = len(ls) - 1
    while index >= 0:
        newlist.append(ls[index])
        index -= 1
    return newlist

ls1 = []
print (reverse(ls1))
ls2 = [3]
print (reverse(ls2))
ls3 = [5,4,3,2,1]
print (reverse(ls3))
########################################
# a function that output a clone list of list s
def clone_ls(s):
    orglist = []
    index = 0
    while index < len(s):
        orglist.append(s[index])
        index += 1
    return orglist

ls1 = []
print (clone_ls(ls1))
ls2 = [3]
print (clone_ls(ls2))
ls3 = [5,6,7,8]
print (clone_ls(ls3))
#####################################
# a function that give the largest number in the list ls
def largest_numb(ls):
    if len(ls) == 0:
        raise ValueError('list cannot be empty')
    max_numb = ls[0]
    index = 0
    for a in ls:
        if max_numb < a:
            max_numb = a
    return max_numb

ls1 = []
try:
    print (largest_numb(ls1))
except ValueError:
    print ('running into error')
ls2 = [45]
print (largest_numb(ls2))
ls3 = [5,4,9,22,3]
print (largest_numb(ls3))
ls4 = [8,9,55,24,3]
print (largest_numb(ls4))
ls5 = [-3,-4,-1]
print (largest_numb(ls5))
#########################################
# Define a running sum of an array as runningSum [i] = sum (nums[0]...nums[i])
def runningSum(ls):
    sum = 0
    nums = []
    for x in ls:
        sum += x
        nums.append(sum)
    return nums
ls1 = []
print (runningSum(ls1))
ls2 = [24]
print (runningSum(ls2))
ls3 = [1,2,3,4]
print (runningSum(ls3))
ls4 = [2,3,4,6]
print (runningSum(ls4))
###########################################
# a function that give the sum of even numbers of the list s
def sum_of_even_numbers(s):
    sum = 0
    index = 0
    while index < len(s):
        if s[index] % 2 == 0:
            sum += s[index]
        index += 1
    return sum

choco = [5,3,2,10,1,4]
print (sum_of_even_numbers(choco))
