from timeit import default_timer as timer

class Breadth_First_Search():
    
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
    
    def bfs_matrix(self, start, goal, matrix):

        #Timer Start
        timerStart = timer()
        queue = [(start, [])]
        #"Closed List"
        exploredNodes = []
        exploredNodes.append(start)
        #Used to insert valid coordinates into queue
        valid_coords = []

        #Order and directions that can can travel up,down,left,right
        directions = list([(-1,0), (1,0), (0,-1), (0,1)]) 

        matrixLen = len(matrix)
        numOfNodesExpanded = 1
        maxNodeMem = 0

        while queue: 
            if timer() - timerStart >= 180:
                print("BFS elapsed time is greater than 3 minutes ")
                exit()
            
            if(maxNodeMem < len(queue)):
                maxNodeMem = len(queue)

            (node, path) = queue.pop(0)

            path.append(node)
            
            if node == goal:
                timerEnd = timer()

                totalTime = (timerEnd - timerStart) * 1000

                self.numNodesExp = numOfNodesExpanded
                self.maxNodesInMem = maxNodeMem
                self.time = totalTime
                self.costPath = findTotalCost(path, matrix)
                self.pathSeq = path

                return 1

            #Goes through neighbors
            for move in directions:
                x_coord = node[0] + move[0] #0?
                y_coord = node[1] + move[1] #3
                
                #CHECK VALUE FOR 0 and check if 
                if x_coord >= 0 and y_coord >= 0 and  x_coord <= matrixLen-1 and y_coord <= matrixLen-1 and matrix[x_coord][y_coord] != 0:
                    valid_coords.append((x_coord,y_coord))
                
            #Adds unexplored nodes in queue
            for child in valid_coords:
                if child not in exploredNodes:
                    exploredNodes.append(child)
                    numOfNodesExpanded += 1

                    queue.append((child, path[:]))  
        
        #Could not find goal
        timerEnd = timer()
        totalTime = (timerEnd - timerStart) * 1000

        self.numNodesExp = numOfNodesExpanded
        self.maxNodesInMem = maxNodeMem
        self.time = totalTime
        self.costPath = -1
        self.pathSeq = "NULL"

        return -1
    
    def print_info(self):
        
        print("Printing out information")
        # Print Cost of path found
        print("1) cost of path: {} ".format(self.costPath))
        # Print number of nodes expanded
        print("2) number of nodes exapanded: {} ".format(self.numNodesExp))
        # Print Maximum number of nodes held in memory
        print("3) maximum number of nodes held in memory: {} ".format(self.maxNodesInMem))
        # print Runtime in Milliseconds 
        print("4) runtime in milliseconds: {} ".format(self.time))
        # Print path
        print("5) path: {} ".format(self.pathSeq))

def findTotalCost(path, matrix):

    totalC = 0
    for node in path:
        totalC += matrix[node[0]][node[1]]

    return totalC
