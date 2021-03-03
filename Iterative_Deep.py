from timeit import default_timer as timer
import Algo_Data

class Iterative_Deep_Search():
    
    def __init__(self):
        self.data = Algo_Data.Algo_Data()
        self.exploredNodesCopy = []
        self.nodesInMem = 0
        
    def __Data__(self):
        return self.data
    
    def IDS(self, src, goal, matrix):

        #Timer Start
        timerStart = timer()

        limit = 0
        cost = 0

        #IDS continues to increase the limit when no solution is found 
        while 1 == 1:
            if timer() - timerStart >= 180:
                print("IDS elapsed time is greater than 3 minutes ")
                exit()

            exploredNodes = []
            exploredNodes.append(src)
            path = []

            #If depth limited search finds the goal it will return 1 as well as all other attributes
            if(self.DLS(src, goal, limit, matrix, exploredNodes, path, cost) == 1):
                path.append(goal)
                self.data.pathSeq = path
                #Adds first and last nodes into the total cost
                self.data.costPath += matrix[goal[0]][goal[1]]
                self.data.costPath += matrix[src[0]][src[1]]
    
                self.data.numNodesExp = len(exploredNodes)

                timerEnd = timer()
                totalTime = (timerEnd - timerStart) * 1000
                self.data.time = totalTime
                return 1

            #Goal is not attainable
            if self.exploredNodesCopy == exploredNodes:
                timerEnd = timer()
                totalTime = (timerEnd - timerStart) * 1000
                self.data.time = totalTime
                self.data.numNodesExp = len(exploredNodes)
        
                self.data.time = totalTime
                self.data.costPath = -1
                self.data.pathSeq = "NULL"
                return 0

            #Saved here to check if all nodes have been explored and goal has not been found
            self.exploredNodesCopy = exploredNodes

            #Start over with a new limit
            cost = 0
            self.data.costPath = 0
            self.data.numNodesExp = 0
            self.nodesInMem = 0
            limit += 1

        return 0

    #Depth Limited Search
    def DLS(self, src, goal, maxDepth, matrix, exploredNodes, path, cost):

        valid_coords = []
        directions = list([(-1,0), (1,0), (0,-1), (0,1)]) 
        matrixLen = len(matrix)

        if src == goal:
            return 1
        
        if maxDepth <= 0:
            return 0

        #Checks each valid neighbor and puts into valid coordinate list
        for move in reversed(directions):
                x_coord = src[0] + move[0] 
                y_coord = src[1] + move[1]
                
                #CHECK VALUE FOR 0 and check if valid coordinates
                if x_coord >= 0 and y_coord >= 0 and  x_coord <= matrixLen-1 and y_coord <= matrixLen-1 and matrix[x_coord][y_coord] != 0:
                    valid_coords.append((x_coord,y_coord))

        #Checks valid children and recurivelsy calls them representing a stack       
        for child in valid_coords:
            if child not in exploredNodes:
                #Adds unexplored nodes stack
                exploredNodes.append(child)

                #Checks for max memory held
                self.nodesInMem += 1
                if (self.data.maxNodesMem < self.nodesInMem):
                    self.data.maxNodesMem = self.nodesInMem

                #Recursively calls iteslf to find the goal node
                if(self.DLS(child, goal, maxDepth-1, matrix, exploredNodes, path, cost)):
                    path.insert(0, src)
                    exploredNodes.append(child)
                    #Calculates total cost of path excluding the first and last
                    self.data.costPath += matrix[child[0]][child[1]]

                    return 1

        #Node was never found (but really this should never go here)
        return 0

    def print_info(self):
        
        print("Printing out information")
        # Print Cost of path found
        print("1) cost of path: {} ".format(self.data.costPath))
        # Print number of nodes expanded
        print("2) number of nodes expanded: {} ".format(self.data.numNodesExp))
        # Print Maximum number of nodes held in memory
        print("3) maximum number of nodes held in memory: {} ".format(self.data.maxNodesMem))
        # print Runtime in Milliseconds 
        print("4) runtime in milliseconds: {} ".format(self.data.time))
        # Print path
        print("5) path: {} ".format(self.data.pathSeq))