import sys
import timeit
import numpy as np
import argparse

#Nicolas Van der Werf, Taeden Anderson
#Did work with each other after class and did not have much of the same code in class.
#No Diagonal Function Used
class NameSearch:

    def __init__(self, Name_List, Name_Algorithm, Name_Length):
        # Matrix of the word search puzzle 
        self.matrix = np.load("./data/matrix.npy")
        # Name of the algorithm
        self.Name_Algorithm = Name_Algorithm
        # Length of the name
        self.Name_Length = Name_Length
        # List of all potential names 
        with open("./data/names/"+Name_List+".txt", 'r') as f:
            self.names = f.read().splitlines()
        self.names = [n.upper().strip() for n in self.names]
        self.Rows, self.Columns = self.matrix.shape

    def match_BruteForce(self, pattern, text):
        # String matching by brute force
        # Your code goes here:
        match = False
        for name in pattern:
            if len(name) == self.Name_Length:
                for i in range(0,len(text)):
                    match = True
                    if name[0] == text[i]:
                        for x in range(0,len(name)):
                            if i + x > len(text) or name[x] != text[i+x]:
                                match = False
                                break
                        if match:
                            returnName = name
                            break
        if match:
            return returnName
        return 'No Name Found'

    def validXY(self,x,y):
        if x < 0 or x >= self.Rows:
            return False
        if y < 0 or y >= self.Columns:
            return False
        return True

    def match_Horspool(self, pattern, text):
        # String matching by Horspool's algorithm
        #pattern is list of names
        #text is text to search
        returnName = ''
        for name in pattern:
            nameLength = len(name)
            # print(name)
            # print(self.Name_Length)
            # print(nameLength == self.Name_Length)

            if nameLength == self.Name_Length:
                # print(name)
                horMap = {chr(i): nameLength for i in range(65, 91)}
                horMap[' '] = nameLength
                # print(horMap)

                for i in range(2,nameLength):
                    c = name[i*-1]
                    # print(c)
                    if horMap[c] == nameLength:
                        horMap[c] = i - 1
                # print(name)
                # print(horMap)
                # return
                i = nameLength - 1
                while i < len(text):
                    # print(i)
                    # namePos = nameLength - 1
                    namePos = 0
                    while namePos <= nameLength-1 and name[nameLength - 1 - namePos] == text[i - namePos]:
                        # print(namePos)
                        namePos += 1
                    if namePos == nameLength:
                        # print(horMap)
                        return name
                    # print(text[textPos])
                    # print(horMap[text[i]], file=sys.stderr)
                    i += horMap[text[i]]

        return 'No Name Found'
        
    def search(self):
        # pattern is each name in self.names
        # text is each horizontal, vertical, and diagonal strings in self.matrix
        text = self.genText()
        # print(text)
        if self.Name_Algorithm == "BruteForce":
            print('-----BRUTEFORCE----', file=sys.stderr)
            result = self.match_BruteForce(self.names, text)
            print(result, end='\r')
            print(result, file=sys.stderr)
        elif self.Name_Algorithm == "Horspool":
            print('-----Horspool----', file=sys.stderr)
            result = self.match_Horspool(self.names, text)
            print(result, end='\r')
            print(result, file=sys.stderr)

    def genText(self):
        returnText = ''
        downCords = [(0, y)for y in range(self.Columns)]
        rightCords = [(x, 0)for x in range(self.Rows)]
        downRightCords = [(x, 0) for x in range(self.Rows)] + [(0,y) for y in range(1,self.Columns)]
        downLeftCords = [(x, self.Columns-1) for x in range(1,self.Rows)] + [(0,y) for y in range(self.Columns)]
        directions = {
            'Down': [1, 0,downCords],
            'Right': [0, 1,rightCords],
            'DownRight': [1, 1,downRightCords],
            'DownLeft': [1, -1,downLeftCords]
        }
        for direction in directions:
            returnText += self.getDirection(directions[direction])
        return returnText



    def getDirection(self,direction):
        text = ' '
        startPoints = direction[2]
        for (x,y) in startPoints:
            for i in range(0,self.Rows+self.Columns):
                posx = x + (i * direction[0])
                posy = y + (i * direction[1])
                if not self.validXY(posx, posy):
                    break
                else:
                    text += self.matrix[posx][posy]
            text += ' '
        return text

    def timeTest(self):
        text = self.genText()
        if self.Name_Algorithm == "BruteForce":
            bf_time = timeit.timeit(lambda: obj.match_BruteForce(self.names, text), number=1)
            print(f"Time: {bf_time:.6f} seconds\n",file=sys.stderr)
        else:
            hp_time = timeit.timeit(lambda: obj.match_Horspool(self.names, text), number=1)
            print(f"Time:   {hp_time:.6f} seconds\n",file=sys.stderr)


if __name__ == "__main__":
        
    parser = argparse.ArgumentParser(description='Word Searching')
    parser.add_argument('-name', dest='Name_List', required = True, type = str, help='Name of name list')
    parser.add_argument('-algorithm', dest='Name_Algorithm', required = True, type = str, help='Name of algorithm')
    parser.add_argument('-length', dest='Name_Length', required = True, type = int, help='Length of the name')
    args = parser.parse_args()

    # Example:
    # python name_search.py -algorithm BruteForce -name Mexican -length 5

    obj = NameSearch(args.Name_List, args.Name_Algorithm, args.Name_Length)
    obj.search()
    obj.timeTest()


