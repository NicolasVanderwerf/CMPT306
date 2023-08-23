"""
Closest pair problem

This returns the closest pair of numbers.

Usage:

    python closest_pair.py [size of list of numbers]

[Nicolas Van der Werf]

[August 23 2023]
"""

import random
import sys

'''
return the distance between two parameters
'''
def distance(a,b):
    return abs(a-b)


'''
populate the array with listSize unique random numbers between 1 ... 5000
'''
def populate(listSize):
    a = []
    count = 0

    while count < listSize:
        number = random.randint(1,5000)
        if number in a:
            continue
        else:
            a.append(number)
            count += 1

    return a

'''
now determine the closest pair
using brute force algorithm
'''
def closest_pair(values):
    closest = distance(values[0], values[1])
    closestPair = [values[0], values[1]]
    x = 0
    for position in values:
        i = 0
        while i < len(values):
            if(i==x):
                i += 1
            else:
                current = distance(position,values[i])
                if current < closest:
                    closestPair = position, values[i]
                    closest = current
                i += 1
        x += 1
    return closestPair




'''
This behaves just like the Java main() method
'''
if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage python Closest.py [number of points]')
        quit()
    else:
        numbers = populate(int(sys.argv[1]))
        print("Number: " + str(numbers))

        closest = closest_pair(numbers)

        print('The closest numbers are', closest[0], 'and', closest[1])
