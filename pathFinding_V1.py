import sys
import map_details
import Breadth_First_Search

def main():
    m = map_details.Map() # create map_details to read input map
    
    file_name = sys.argv[1] # get input file

    if "BFS" == sys.argv[2]:
        algo = Breadth_First_Search.Breadth_First_Search()
    elif 'IDS' == sys.argv[2]:
        pass
    elif 'A*' == sys.argv[2]: 
        pass
    else:
        print("PlEASE PUT CORRECT PARAMETERS")
        exit()
    
    f = open(file_name)
    m.read_file(f)
    
    start_loc = tuple(map(int, m.starting_loc.split(' ')))
    goal = tuple(map(int, m.goal.split(' ')))
    
    algo.bfs_matrix(start_loc,goal,m.matrix)
    if algo.bfs_matrix(start_loc,goal,m.matrix) == 1:
        algo.print_info()
    else:
        algo.print_info()
        print("Could not find the goal node")

main()