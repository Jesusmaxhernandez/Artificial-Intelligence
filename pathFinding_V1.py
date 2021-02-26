import map_details
#import Breadth_First_Search
 

inMatrix = [[2,4,2,1,4,5,2], 
            [0,1,2,3,5,3,1], 
            [2,0,4,4,1,2,4], 
            [2,5,5,3,2,0,1], 
            [4,3,3,2,1,0,1]]

#print(inMatrix[1,2])
#dimensions, starting_loc, goal, matrix = map.read_map()
#Breadth_First_Search.bfs_matrix(starting_loc,goal,matrix

x = map_details.Map()
x.read_file()


print(x.dimensions)
print(x.goal)
print(x.matrix)

#print(rm.__dimensions__())
#rm.read_file()

#print(inMatrix[path[0]])
#solution given - [(1, 2), (2, 1), (3, 2), (4, 3)] non zero based
# zero based - [(0, 1), (1, 0), (2, 1), (3, 2)] 
    