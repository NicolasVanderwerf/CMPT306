
import random

#For each, For each, check if in output list, add if not

# check if both lists are greater than 0
# create return list
#for i in range length of first list
    #if list1[i] in list2 and list1[i] is not in the return list
        # add it to the return list
    # return the return List
# if both lists are not greater than 0 print an exception

def findCommon(list1,list2):
    returnList = []
    if len(list1) > 0 and len(list2) > 0:
        for element in list1:
            if element in list2 and element not in returnList:
                returnList.append(element)
        return returnList
    else:
        return returnList

listA = [1,2,3,4,5,6,6,6,7,8,9]
listB = [1,7,4,2,6,6,6,6,6,6]

print(findCommon(listA, listB))

listC = []
for i in range(0,1000):
    listC.append(random.randrange(10000))

listD = []
for i in range(0,100):
    listD.append(random.randrange(10000))

if len(findCommon(listC,listD)) > 0:
    print("Worked?")
else:
    print("borke?")

listE = [1,2,3,4,5,6,7,8,9]
listF = []
print(findCommon(listE,listF))


print("---------------------------------")
# check if 0 and return '0'
#CHeck if number is even
#while number is greater then 1
#    modulo by 2 and add a 1 to binary if remainder is 0, add 0 to binary if remainder is 1


def findBinary(number):
    binary = []
    while number != 0:
        if (number % 2) == 0:
            binary.insert(0,0)
            number = number // 2
        else:
            binary.insert(0,1)
            number = (number - 1) // 2
    return binary


print(findBinary(16))
