import sys
import map_details
#import Breadth_First_Search

def get_args():

    file_name = sys.argv[1] # get input file

    if "BFS" == sys.argv[2]:
        algroithim_to_run = 'bfs'
        print("BFS!")
    elif 'IDS' == sys.argv[2]:
        algroithim_to_run = 'ids'
    elif 'A*' == sys.argv[2]: 
        algroithim_to_run = 'A*'

    m = map_details.Map()
    f = open(file_name)
    m.read_file(f)
    

get_args()