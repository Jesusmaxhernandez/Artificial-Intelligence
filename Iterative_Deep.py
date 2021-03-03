from timeit import default_timer as timer

class Iterative_Deep_Search():
    
    def __init__(self):
        self.costPath = 0 
        self.numNodesExp = 0
        self.maxNodesMem = 0
        self.time = 0
        self.pathSeq = []
        self.exploredNodesCopy = []

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
        depth = 0

        while queue: 
            if timer() - timerStart >= 180:
                print("IDS elapsed time is greater than 3 minutes ")
                exit()
            
            if(maxNodeMem < len(queue)):
                maxNodeMem = len(queue)

            print("THIS IS THE Child: ", queue)
           

            (node, path) = queue.pop()

            print("This is what is popped: ", (node, path))

            path.append(node)
            
            if node == goal:
                timerEnd = timer()

                totalTime = (timerEnd - timerStart) * 1000

                self.numNodesExp = numOfNodesExpanded
                self.maxNodesInMem = maxNodeMem
                self.time = totalTime
                self.costPath = findTotalCost(path, matrix)
                self.pathSeq = path

                print("THIS IS THE DEPTH: " , depth)

                return 1

            #Goes through neighbors
            for move in directions:
                x_coord = node[0] + move[0] 
                y_coord = node[1] + move[1] 
                
                #CHECK VALUE FOR 0 and check if 
                if x_coord >= 0 and y_coord >= 0 and  x_coord <= matrixLen-1 and y_coord <= matrixLen-1 and matrix[x_coord][y_coord] != 0:
                    valid_coords.append((x_coord,y_coord))

            depth += 1

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
    
    def IDS(self, src, target, matrix):

        #Timer Start
        timerStart = timer()

        limit = 0
        cost = 0

        while 1 == 1:
            exploredNodes = []
            exploredNodes.append(src)
            path = []

            if(self.DLS(src, target, limit, matrix, exploredNodes, path, cost) == 1):
                print("FOUND THE NODE at DEPTH: ", limit)
                path.append(target)
                self.pathSeq = path
                self.costPath += matrix[target[0]][target[1]]
                self.costPath += matrix[src[0]][src[1]]
                timerEnd = timer()

                totalTime = (timerEnd - timerStart) * 1000
                self.time = totalTime
                return 1

            # if self.exploredNodesCopy == exploredNodes:
            #     return 0
            
            # self.exploredNodesCopy = exploredNodes

            cost = 0
            self.costPath = 0
            self.numNodesExp = 0
            limit += 1

        return 0

    def DLS(self, src, target, maxDepth, matrix, exploredNodes, path, cost):

        valid_coords = []

        directions = list([(-1,0), (1,0), (0,-1), (0,1)]) 
        matrixLen = len(matrix)

        if src == target:
            print("Depth: " , maxDepth)
            return 1
        
        if maxDepth <= 0:
            return 0

        for move in reversed(directions):
                x_coord = src[0] + move[0] 
                y_coord = src[1] + move[1]
                
                #CHECK VALUE FOR 0 and check if valid coordinates
                if x_coord >= 0 and y_coord >= 0 and  x_coord <= matrixLen-1 and y_coord <= matrixLen-1 and matrix[x_coord][y_coord] != 0:
                    valid_coords.append((x_coord,y_coord))
                
        for child in valid_coords:
            if child not in exploredNodes:
                #Adds unexplored nodes in queue
                exploredNodes.append(child)
                if(self.DLS(child, target, maxDepth-1, matrix, exploredNodes, path, cost)):
                    print("SUCCESS node", src, " THsi is the depth: ", maxDepth)
                    path.insert(0, src)
                    exploredNodes.append(child)
                    self.costPath += matrix[child[0]][child[1]]
                    print("THIS IS COST: ", cost)
                    return 1
                #exploredNodes.append(child)
                print("THis the node", src, " THsi is the depth: ", maxDepth)
                #numOfNodesExpanded += 1
                self.numNodesExp += 1

                # queue.append((child, path[:]))  

        # for i in matrix[src]:
        #     if(self.DLS(i, target, maxDepth-1, matrix)):
        #         return 1
        # for move in directions:
            
        #     x_coord = src[0] + move[0] 
        #     y_coord = src[1] + move[1] 

        #     print("this is x: ", x_coord)
        #     print("this is y: ", y_coord)

            # for child in valid_coords:
            #     if child not in exploredNodes:
            #         exploredNodes.append(child)
            #         numOfNodesExpanded += 1

            #         queue.append((child, path[:]))  
            
            #CHECK VALUE FOR 0 and check if 
            # if x_coord >= 0 and y_coord >= 0 and  x_coord <= matrixLen-1 and y_coord <= matrixLen-1 and matrix[x_coord][y_coord] != 0:
            #     if src not in eN:
            #         if(self.DLS(move, target, maxDepth-1, matrix, eN)):
            #             print("SUCCESS node", src, " THsi is the depth: ", maxDepth)
            #             return 1
            #         eN.append(src)
            #         print("THis the node", src, " THsi is the depth: ", maxDepth)
        print("en: ", exploredNodes)
        return 0

    def print_info(self):
        
        print("Printing out information")
        # Print Cost of path found
        print("1) cost of path: {} ".format(self.costPath))
        # Print number of nodes expanded
        print("2) number of nodes expanded: {} ".format(self.numNodesExp))
        # Print Maximum number of nodes held in memory
        # print("3) maximum number of nodes held in memory: {} ".format(self.maxNodesInMem))
        # print Runtime in Milliseconds 
        print("4) runtime in milliseconds: {} ".format(self.time))
        # Print path
        print("5) path: {} ".format(self.pathSeq))