import sys
import map_details
#import Breadth_First_Search
 

inMatrix = [[2,4,2,1,4,5,2], 
            [0,1,2,3,5,3,1], 
            [2,0,4,4,1,2,4], 
            [2,5,5,3,2,0,1], 
            [4,3,3,2,1,0,1]]

x = map_details.Map()
#x.read_file()


print(x.dimensions)
print(x.goal)
print(x.matrix)
 
def get_args():

    input_file_name = sys.argv[1] # get input file
    print(input_file_name)
    print(sys.argv[2])

    if "BFS" == sys.argv[2]:
        algroithim_to_run = 'bfs'
        print("BFS!")
    elif 'IDS' == sys.argv[2]:
        algroithim_to_run = 'ids'
    elif 'A*' == sys.argv[2]: 
        algroithim_to_run = 'A*'

get_args()