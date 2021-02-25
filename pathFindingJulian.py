
def bfs_matrix(start, goal, matrix):
    queue = [(start, [])]
    explored = []
    exploredValue = []
    coords_can_visit = []
    directions = list([(-1,0), (1,0), (0,-1), (0,1)]) # Order and directions that can can travel up,down,left,right
    N = len(matrix)

    while queue:
        (node, path) = queue.pop(0)
        path.append(node)
        
        if node == goal:
            print(explored)
            return path
            
        explored.append(node)
        #exploredValue.append() testing to find values and not coordinates


        for move in directions:
            x_coord = node[0] + move[0]
            y_check = node[1] + move[1]
            
            if x_coord >= 0 and y_check >= 0 and  x_coord <= N-1 and y_check <= N-1:
               coords_can_visit.append((x_coord,y_check))
               

        for child in coords_can_visit:
            if child not in explored:
                queue.append((child, path[:]))
                
                

    return None


inMatrix = [[2,4,2,1,4,5,2], 
            [0,1,2,3,5,3,1], 
            [2,0,4,4,1,2,4], 
            [2,5,5,3,2,0,1], 
            [4,3,3,2,1,0,1]]

#print(inMatrix[1,2])

print(inMatrix)
path = (bfs_matrix((1, 2), (0, 3), inMatrix))
print(path)

#print(inMatrix[path[0]])
#solution given - [(1, 2), (2, 1), (3, 2), (4, 3)] non zero based
# zero based - [(0, 1), (1, 0), (2, 1), (3, 2)]