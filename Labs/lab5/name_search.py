import numpy as np 
import argparse

from tqdm import tqdm


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
        pass

    def match_BruteForce2(self):
        Rows, Columns = self.matrix.shape
        pbar = tqdm(self.names, bar_format='{rate_fmt}')
        for name in pbar:
            if len(name) == self.Name_Length:
                for x in range(0,self.Rows):
                    for y in range(0,self.Columns):
                        if self.matrix[x, y] == name[0]:
                            valid = self.BruteForceSearch(name,x,y)
                            if valid[0] == True:
                                return valid[1]
    def BruteForceSearch(self,name,x,y):
        valid = False, ''
        lName = len(name) - 1

        directions = [
            ('Down', (1, 0)),
            ('Right', (0, 1)),
            ('DownRight', (1, 1)),
            ('DownLeft', (1, -1))
        ]

        for direction,(dirx,diry) in directions:
            endx = x+(lName*dirx)
            endy = y+(lName*diry)
            if self.validXY(endx,endy) and self.matrix[endx, endy] == name[lName]:
             for i in range(1,len(name)):
                 posx = x + (i * dirx)
                 posy = y + (i * diry)
                 if self.validXY(posx,posy) and self.matrix[posx, posy] != name[i]:
                     valid = False, ''
                     break
                 else:
                     valid = True, name+' True '+direction+': ' + str(x + 1) + ' ' + str(y + 1)
        return valid

    def validXY(self,x,y):
        if x < 0 or x >= self.Rows:
            return False
        if y < 0 or y >= self.Columns:
            return False
        return True

    def match_Horspool(self, pattern, text):
        # String matching by Horspool's algorithm
        # Your code goes here:
        pass
        
    def search(self):
        # pattern is each name in self.names
        # text is each horizontal, vertical, and diagonal strings in self.matrix 
        if self.Name_Algorithm == "BruteForce":
            # call self.match_BruteForce(pattern, text)
            nameLocation = self.match_BruteForce2()
            print(nameLocation)
            #print(self.matrix)
            pass
        elif self.Name_Algorithm == "Horspool":
            # call self.match_Horspool(pattern, text)
            pass

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


