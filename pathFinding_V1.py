import sys
import map_details
import Breadth_First_Search
import Iterative_Deep
import A_Star

def main():
    # Create map_details to read input map
    map_Data = map_details.Map() # create map_details to read input map
    
    # Get Input File 
    file_name = sys.argv[1] # 

    if "BFS" == sys.argv[2]:
        algo = Breadth_First_Search.Breadth_First_Search()
    elif 'IDS' == sys.argv[2]:
        algo = Iterative_Deep.Iterative_Deep_Search()
    elif 'AS' == sys.argv[2]: 
        algo = A_Star.A_Star()
    else:
        print("PlEASE PUT CORRECT PARAMETERS")
        exit()
    
    f = open(file_name)
    map_Data.read_file(f)
    
    start_loc = tuple(map(int, map_Data.starting_loc.split(' ')))
    goal = tuple(map(int, map_Data.goal.split(' ')))
    
    
    
    if "BFS" == sys.argv[2]:
        if algo.bfs_matrix(start_loc,goal,map_Data.matrix) == 1:
            algo.print_info()
        else:
            algo.print_info()
            print("Could not find the goal node")

    elif 'IDS' == sys.argv[2]:
        if algo.IDS(start_loc,goal,map_Data.matrix) == 1:
            algo.print_info()
        else:
            algo.print_info()
            print("Could not find the goal node")

    elif 'AS' == sys.argv[2]: 
        if algo.a_star_matrix(start_loc,goal,map_Data.matrix) == 1:
            algo.print_info()
        else:
            algo.print_info()
            print("Could not find the goal node")
    else:
        print("PlEASE PUT CORRECT PARAMETERS")
        exit()
    

if __name__ == '__main__':
    main()