from timeit import default_timer as timer

class Breadth_First_Search:
    
    def __init__(self):
        print("Hi")

    
    def bfs_matrix(self, start, goal, matrix):

        #Timer Start
        timerStart = timer()
        queue = [(start, [])]
        exploredNodes = []
        exploredNodes.append(start)
        valid_coords = []

        #Order and directions that can can travel up,down,left,right
        directions = list([(-1,0), (1,0), (0,-1), (0,1)]) 

        matrixLen = len(matrix)
        numOfNodes = 1
        maxNodeMem = 0

        while queue: 

            if(maxNodeMem < len(queue)):
                maxNodeMem = len(queue)

            (node, path) = queue.pop(0)

            # print(node, " this is node")
            # print(node, ", this is path")

            path.append(node)
            
            if node == goal:
                print("Number of nodes expanded", numOfNodes)
                print("Maximimum number of nodes held in memory: ", maxNodeMem)
                return (path)

            for move in directions:
                x_coord = node[0] + move[0] #0?
                y_coord = node[1] + move[1] #3
                
                #CHECK VALUE FOR 0 and check if 
                if x_coord >= 0 and y_coord >= 0 and  x_coord <= matrixLen-1 and y_coord <= matrixLen-1 and matrix[x_coord][y_coord] != 0:
                    valid_coords.append((x_coord,y_coord))
                

            for child in valid_coords:
                # print("This is exploredNodes BEFORE: ", exploredNodes)
                # print("this is children BEFORE: ", child)
                if child not in exploredNodes:
                    exploredNodes.append(child)
                    numOfNodes += 1
                    # print("This is exploredNodes: ", exploredNodes)
                    # print("this is children", child)
                    queue.append((child, path[:]))
                    
        return None


        
print(inMatrix)
path = (bfs_matrix((1, 2), (4,3), inMatrix))
print("Sequence of coordinates: ", path)


def findTotalCost(path, matrix):

    totalC = 0
    for node in path:
        # print(node, " this is nodesss")
        totalC += matrix[node[0]][node[1]]

    return totalC

print("This is the total cost of the path found: ", findTotalCost(path, inMatrix))