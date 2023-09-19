
'''
Demonstration of some simple graph algorithms.
    
@author: Jingsai Liang
'''

import sys

class GraphAlgorithms:
    
    '''
    Reads in the specified input file containing
    adjacent edges in a graph and constructs an
    adjacency list.

    The adjacency list is a dictionary that maps
    a vertex to its adjacent vertices.
    '''
    def __init__(self, fileName): 
        self.visited = {}
        graphFile = open(fileName)

        '''
        create an initially empty dictionary representing
        an adjacency list of the graph
        '''
        self.adjacencyList = { }
    
        '''
        collection of vertices in the graph (there may be duplicates)
        '''
        self.vertices = [ ]

        for line in graphFile:
            '''
            Get the two vertices
        
            Python lets us assign two variables with one
            assignment statement.
            '''
            (firstVertex, secondVertex) = line.split()
        
            '''
            Add the two vertices to the list of vertices
            At this point, duplicates are ok as later
            operations will retrieve the set of vertices.
            '''
            self.vertices.append(firstVertex)
            self.vertices.append(secondVertex)

            '''
            Check if the first vertex is in the adjacency list.
            If not, add it to the adjacency list.
            '''
            if firstVertex not in self.adjacencyList:
                self.adjacencyList[firstVertex] = [ ]

            '''
            Add the second vertex to the adjacency list of the first vertex.
            '''
            self.adjacencyList[firstVertex].append(secondVertex)
        
        # creates and sort a set of vertices (removes duplicates)
        self.vertices = list(set(self.vertices))
        self.vertices.sort()

        # sort adjacency list for each vertex
        for vertex in self.adjacencyList:
            self.adjacencyList[vertex].sort()

    '''
    Begins the DFS algorithm.
    '''
    def DFSInit(self):
        # initially all vertices are considered unknown
        self.visited = {v: False for v in self.vertices}
        # initialize path as an empty string
        self.path = ""

    '''
    depth-first traversal of specified graph
    '''
    def DFS(self, method):
        self.DFSInit()
        if method == 'recursive':
            for v in self.vertices:
                if not self.visited[v]:
                    self.DFS_recur(v)
            return self.path

        elif method == 'stack':
            # Your code goes here:
            self.path = ''
            self.visited = {v: False for v in self.vertices}
            for v in self.vertices:
                if not self.visited[v]:
                    self.DFS_stack(v)

            return self.path
            

    def DFS_recur(self,vertex):
        adjacentV = self.adjacencyList[vertex]
        self.path = self.path + vertex
        self.visited[vertex] = True
        for v in adjacentV:
            if not self.visited[v]:
                self.DFS_recur(v)
                
    def DFS_stack(self, vertex):

        stack=[]
        stack.insert(0,vertex)
        while len(stack) > 0:
            v = stack.pop(0)
            if not self.visited[v]:
                self.path = self.path + v
                self.visited[v] = True
                for a in self.adjacencyList[v]:
                    if not self.visited[a]:
                        stack.insert(0, a)
        # Your code goes here:





    def BFSInit(self):
        # initially all vertices are considered unknown
        self.visited = {v: False for v in self.vertices}
        # initialize path as an empty string
        self.path = ""
        

    def BFS(self):
        self.BFSInit()
        self.path = ''
        for v in self.vertices:
            if not self.visited[v]:
                self.BFSrun(v)

        return self.path
    def BFSrun(self,vertex):
        queue = []
        queue.append(vertex)
        while len(queue) > 0:
            v = queue.pop(0)
            if not self.visited[v]:
                self.path = self.path + v
                self.visited[v] = True
                for a in self.adjacencyList[v]:
                    if not self.visited[a]:
                        queue.append(a)

    def hasCycleinit(self):
        self.visited = {v: False for v in self.vertices}
    def hasCycle(self):
        self.hasCycleinit()
        for v in self.vertices:
            if not self.visited[v]:
                if self.hasCycleR(v):
                    return True
        return False

    def hasCycleR(self, vertex, parent=None):
        self.visited[vertex] = True
        for v in self.adjacencyList[vertex]:
            if not self.visited[v]:
                if self.hasCycleR(v, vertex):
                    return True
            elif v != parent:
                return True

        return False

    # Work on this function for at most 10 extra points
    def shortestpath(self, p, q):
        self.visited = {v: False for v in self.vertices}
        queue = []
        queue.append(p)
        queue.append('level')
        i = 0
        while len(queue) > 0:
            v = queue.pop(0)
            if v == 'level':
                i += 1
                if len(queue) > 0:
                    queue.append('level')
            elif v == q:
                return i
            else:
                if not self.visited[v]:
                    self.visited[v] = True
                    for a in self.adjacencyList[v]:
                        if not self.visited[a]:
                            queue.append(a)
                
        

        

