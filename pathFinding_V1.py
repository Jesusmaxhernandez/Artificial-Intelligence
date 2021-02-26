import sys
import map_details
import Breadth_First_Search

def get_args():
    m = map_details.Map() # create map_details to read input map
    
    file_name = sys.argv[1] # get input file

    if "BFS" == sys.argv[2]:
        algo = Breadth_First_Search.Breadth_First_Search()
    elif 'IDS' == sys.argv[2]:
        pass
    elif 'A*' == sys.argv[2]: 
        pass
    
    f = open(file_name)
    m.read_file(f)
    
    start_loc = tuple(map(int, m.starting_loc.split(' ')))
    goal = tuple(map(int, m.goal.split(' ')))
    
    
    algo.bfs_matrix(start_loc,goal,m.matrix)
    algo.print_info()

get_args()