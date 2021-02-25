
def bfs_matrix(start, goal, matrix):
    queue = [(start, [])]

    explored = []
    explored.append(start)
    exploredValue = []
    coords_can_visit = []
    directions = list([(-1,0), (1,0), (0,-1), (0,1)]) # Order and directions that can can travel up,down,left,right
    N = len(matrix)
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
            #print("This is explored", explored)
            print("Number of nodes expanded", numOfNodes)
            print("Maximimum number of nodes held in memory: ", maxNodeMem)
            return (path)

        for move in directions:
            x_coord = node[0] + move[0] #0?
            y_check = node[1] + move[1] #3
            
            #CHECK VALUE FOR 0
            if x_coord >= 0 and y_check >= 0 and  x_coord <= N-1 and y_check <= N-1 and matrix[x_coord][y_check] != 0:
               coords_can_visit.append((x_coord,y_check))
               

        for child in coords_can_visit:
            # print("This is explored BEFORE: ", explored)
            # print("this is children BEFORE: ", child)
            if child not in explored:
                explored.append(child)
                numOfNodes += 1
                # print("This is explored: ", explored)
                # print("this is children", child)
                queue.append((child, path[:]))
                
    return None

inMatrix = [[2,4,2,1,4,5,2], 
            [0,1,2,3,5,3,1], 
            [2,0,4,4,1,2,4], 
            [2,5,5,3,2,0,1], 
            [4,3,3,2,1,0,1]]

#print(inMatrix[1,2])

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
#print(inMatrix[path[0]])
#solution given - [(1, 2), (2, 1), (3, 2), (4, 3)] non zero based
# zero based - [(0, 1), (1, 0), (2, 1), (3, 2)]

