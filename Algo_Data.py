class Algo_Data():
    
    def __init__(self):
        self.costPath = 0 
        self.numNodesExp = 0
        self.maxNodesMem = 0
        self.time = 0
        self.pathSeq = []

    def __costPath__(self):
        return self.costPath

    def __numNodesExp__(self):
        return self.numNodesExp
    
    def __maxNodeMem__(self):
        return self.maxNodesInMem
    
    def __time__(self):
        return self.time
    
    def __pathSeq__(self):
        return self.pathSeq

    def findTotalCost(self, path, matrix):
        totalC = 0
        for node in path:
            totalC += matrix[node[0]][node[1]]

        self.costPath = totalC

    
    def print_info(self):
        
        print("Printing out information")
        # Print Cost of path found
        print("1) cost of path: {} ".format(self.costPath))
        # Print number of nodes expanded
        print("2) number of nodes expanded: {} ".format(self.numNodesExp))
        # Print Maximum number of nodes held in memory
        print("3) maximum number of nodes held in memory: {} ".format(self.maxNodesInMem))
        # print Runtime in Milliseconds 
        print("4) runtime in milliseconds: {} ".format(self.time))
        # Print path
        print("5) path: {} ".format(self.pathSeq))    