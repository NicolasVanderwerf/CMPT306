'''
    CoPrime.py

    Generates a graph of the m x n co-primes
    
    [YOUR NAME GOES HERE]
'''

import sys

'''
generates the co-primes in an m x n matrix
'''
def coprimes(m, n):
    '''
    creates a list of size n each with
    each element initialized to None
    '''
    result = [None] * (m + 1)

    '''
    each element in the list is now a
    list of size m where each value
    is initialized to a space ' '
    '''
    for i in range(0,m+1):
        result[i] = ['^'] * (n + 1)
        
    '''
    output the contents of result
    '''
    row = 0
    col = 0
    for x in result:
        # x[:] is a list "slice"
        for y in x[:]:
            # print("ROW: " +str(row) + " COL: " + str(col) + "   IS COPRIME:  " + str(isCoPrime(row,col)))
            if isCoPrime(row,col):
                print('   ', end="")
            else:
                print(y + '  ', end="")
            row += 1
        row = 0
        col += 1


        print()

    '''
        YOUR WORK WILL GO HERE
    '''
def isCoPrime(x,y):
    small = 0
    large = 0
    if x < y:
        small, large = x, y
    else:
        small, large = y, x
    for z in range(2, small+1):
        # print("iter: " + str(z) + "  small mod: " + str(small % z) + " Big mod: " + str(large % z))
        if small % z == 0 and large % z == 0:
            return False
    return True


# behaves like main() method

if __name__ == "__main__":
    # some error checking
    if len(sys.argv) != 3:
        print('Usage\n python CoPrime [int] [int]')
        quit()

    #coprimes(int(sys.argv[1]), int(sys.argv[2]))

