from timeit import default_timer as timer
import Algo_Data
class Breadth_First_Search():
    
    def __init__(self):
        self.data = Algo_Data.Algo_Data()
    
    def __Data__(self):
        return self.data 

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

                self.data.numNodesExp = numOfNodesExpanded
                self.data.maxNodesInMem = maxNodeMem
                self.data.time = totalTime
                #self.data.costPath = findTotalCost(path, matrix)
                self.data.findTotalCost(path,matrix)
                self.data.pathSeq = path
                #Algo_Data.print_info()

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
        self.data.print_info()


