import argparse
from itertools import permutations
import math

from tqdm import tqdm

from draw import draw_path
from test import test_path

class password():
    def __init__(self, rule):
        self.rule = rule
        # Longest distance
        self.longest_length = 0.0
        # List of longest path. The longest path is not unique. 
        self.longest_path = []
        # Your code goes here:
        self.perms = []
        p = permutations("123456789")
        for i in p:
            self.perms.append(''.join(i))
        self.invalidCross = ['73','37','28','82','19','91','46','64']
        self.coords = {7:(0, 2), 8:(1, 2), 9:(2, 2), 4:(0, 1), 5:(1, 1), 6:(2, 1), 1:(0, 0), 2:(1, 0), 3:(2, 0)}




    # Find the longest path
    def find_longest_path(self):
        if self.rule == 1:
            self.rule1()
        else:
            self.rule2()

    def rule1(self):
        pbar = tqdm(self.perms, desc="Processing codes")
        for p in pbar:
            valid = True
            for x in self.invalidCross:
                if x in p:
                    valid = False
            if valid:
                length = self.totalDistance(p)
                if length > self.longest_length:
                    self.longest_path = []
                    self.longest_path.append(p)
                    self.longest_length = length
                elif length == self.longest_length:
                    self.longest_path.append(p)


    def rule2(self):
        pbar = tqdm(self.perms, desc="Checking Permutations")
        for p in pbar:
            valid = True
            for x in self.invalidCross:
                if x in p:
                    if p.index(x) > p.index('5'):
                        valid = True
                    else:
                        valid = False
            if valid:
                length = self.totalDistance(p)
                if length > self.longest_length:
                    self.longest_path = []
                    self.longest_path.append(p)
                    self.longest_length = length
                elif length == self.longest_length:
                    self.longest_path.append(p)


    def totalDistance(self,path):
        length = 0
        for i in range(0,len(path)-1):
            length += self.distance(self.coords[int(path[i])],self.coords[int(path[i+1])])
        return length
  
    # Calculate distance between two vertices
    # Format of a coordinate is a tuple (x_value, y_value), for example, (1,2), (0,1)
    def distance(self, vertex1, vertex2):
        return math.sqrt((vertex1[0]-vertex2[0])**2 + (vertex1[1]-vertex2[1])**2)

    # Print and save the result
    def print_result(self):
        print("The longest length using rule " + str(self.rule) + " is:")
        print(self.longest_length)
        print()
        print("All paths with longest length using rule " + str(self.rule) + " are:") 
        print(self.longest_path)
        print()
        with open('results_rule'+str(self.rule)+'.txt', 'w') as file_handler:
            file_handler.write("{}\n".format(self.longest_length)) 
            for path in self.longest_path:
                file_handler.write("{}\n".format(path)) 

    # test the result 
    def test(self):
        test_path(self.longest_length, self.longest_path, self.rule)

    # draw first result
    def draw(self):
        if len(self.longest_path) > 0:
            draw_path(self.longest_path[0], self.rule)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='PatternLock')
    parser.add_argument('-rule', dest='rule', required = True, type = int, help='Index of the rule')
    args = parser.parse_args()

    # usage
    # python PatternLock.py -rule 1
    # python PatternLock.py -rule 2
    
    # Initialize the object using rule 1 or rule 2
    run = password(args.rule)
    # Find the longest path
    run.find_longest_path()
    # Print and save the result
    run.print_result()
    # Draw the first longest path
    #run.draw()
    # Verify the result 
    run.test()