# CLASS AUGUST 28 2023
import random

a = [1,2,3,4,5,6,7,8,9]
b = [11,7,4,3,9]
c = [0]
d = []


def findBiggest(list):
    if len(list) > 0:
        biggest = list[0]
        for number in list:
            if number > biggest:
                biggest = number
        print("Biggest:  " + str(biggest))
    else:
        print("List is Empty")

findBiggest(a)
findBiggest(b)
findBiggest(c)
findBiggest(d)

e = []
for i in range(0,100000):
    e.append(random.randrange(10000))
findBiggest(e)


