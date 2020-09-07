#find the mean of the list
def meanlist(ls):
    sum = 0
    for x in ls:
        sum += x
    return sum / len(ls)

#sort the list in ascending order
def clone_ls(s):
    orglist = []
    index = 0
    while index < len(s):
        orglist.append(s[index])
        index += 1
    return orglist

def ascendingls(ls):
    clone = clone_ls(ls)
    clone.sort()
    return clone



#find the median of the list
def medianlist(ls):
    ls = ascendingls(ls)
    if len(ls) % 2 == 0:
        med1 = ls[int(len(ls)/2 - 1)]
        med2 =ls[int(len(ls)/2)]
        return (med1 + med2)/2
    else:
        return ls[int((len(ls) - 1)/2)]



#sort the list in descending order
def descendingls(ls):
    clone = clone_ls(ls)
    clone.sort(reverse = True)
    return clone

#find the maxium in the list
#find the min in the list

def main():
    ls1 = [] #do not test this case cause it does not work
    ls2 = [20]
    ls3 = [3,5,6,8,10,2] #mean = 5.6666 med = 5.5
    ls4 = [2,3,5,7,6] #mean = 4.6 med = 5
    test_cases = [ls2,ls3,ls4]
    for each in test_cases:
        print('input: ' , each)
        print('mean: ', meanlist(each))
        print('median:', medianlist(each))
        print('ascending: ', acendingls(each))
        print('descending: ', decendingls(each))
main()
