import sys
import map_details
import Breadth_First_Search

def get_args():
    m = map_details.Map()
    bfs = Breadth_First_Search.Breadth_First_Search()
    file_name = sys.argv[1] # get input file

    if "BFS" == sys.argv[2]:
        algroithim_to_run = 'bfs'
    elif 'IDS' == sys.argv[2]:
        algroithim_to_run = 'ids'
    elif 'A*' == sys.argv[2]: 
        algroithim_to_run = 'A*'

    f = open(file_name)
    m.read_file(f)
    start_loc = tuple(map(int, m.starting_loc.split(' ')))
    goal = tuple(map(int, m.goal.split(' ')))
    #print(bfs.bfs_matrix(start_loc,goal,m.matrix))

    # Print Cost of path found

    # Print number of nodes expanded

    # Print Maximum number of nodes held in memory

    # print Runtime in Milliseconds 

    # Print path

def print_info():



get_args()