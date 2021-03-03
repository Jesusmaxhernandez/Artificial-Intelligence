import Node
import Algo_Data
from timeit import default_timer as timer

# Code based off https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2


class A_Star():
    def __init__(self):
        self.data = Algo_Data.Algo_Data()
    
    def __Data__(self):
        return self.data
    
    def a_star_matrix(self, start, end, maze):   
        # Timer Start
        timerStart = timer()

        # Max Nodes expanded
        numOfNodesExpanded = 1
        
        # Max nodes in memory
        maxNodeMem = 0

        # Create start and end node
        start_node = Node.Node(None, start)
        start_node.g = start_node.h = start_node.f = 0
        end_node = Node.Node(None, end)
        end_node.g = end_node.h = end_node.f = 0

        # Initialize both open and closed list
        open_list = []
        closed_list = []

        # Add the start node
        open_list.append(start_node)

        # Loop until you find the end
        while len(open_list) > 0:
            # Start Timer 
            if timer() - timerStart >= 180:
                print("BFS elapsed time is greater than 3 minutes ")
                exit()

            # Get max number of nodes in memory 
            if(maxNodeMem < len(open_list)):
                maxNodeMem = len(open_list)


            # Get the current node
            current_node = open_list[0]
            current_index = 0
            for index, item in enumerate(open_list):
                if item.f < current_node.f:
                    current_node = item
                    current_index = index

            # Pop current off open list, add to closed list
            open_list.pop(current_index)
            closed_list.append(current_node)

            # Found the goal
            if current_node == end_node:
                # End the timer
                timerEnd = timer()
                totalTime = (timerEnd - timerStart) * 1000
               

               # Add append path from node to list
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                
                self.data.numNodesExp = numOfNodesExpanded
                self.data.maxNodesInMem = maxNodeMem
                self.data.time = totalTime
                self.data.findTotalCost(path,maze)
                # Return reversed path
                self.data.pathSeq = path[::-1] 
                return 1 

            # Generate children
            children = []
            # Adjacent squares in order of up, down, left, right
            for new_position in [(-1,0), (1,0), (0,-1), (0,1)]: # Adjacent squares

                # Get node position
                node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

                # Make sure within range
                if node_position[0] > (len(maze) - 1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                    continue

                # Make sure walkable terrain only with 0 being impassable 
                if maze[node_position[0]][node_position[1]] <= 0 :
                    continue

                # Create new node
                new_node = Node.Node(current_node, node_position)

                # Append
                children.append(new_node)

            # Loop through children
            for child in children:

                # Child is on the closed list
                # for closed_child in closed_list:
                if child in closed_list:
                    continue
                # Initilize two parameters for heuristic (manhattan Distance)
                neighbors = child.position[0],child.position[1]
                goalNode = end_node.position[0],end_node.position[1]
                
                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = heuristic(neighbors, goalNode)  
                child.f = child.g + child.h

                # Child is already in the open list
                if child in open_list: 
                    continue

                # Add the child to the open list
                open_list.append(child)

                # Increment number of nodes expanded
                numOfNodesExpanded += 1
        
        #Could not find goal
        timerEnd = timer()
        totalTime = (timerEnd - timerStart) * 1000

        self.dataanumNodesExp = numOfNodesExpanded
        self.data.maxNodesInMem = maxNodeMem
        self.data.time = totalTime
        self.data.costPath = -1
        self.data.pathSeq = "NULL"
        return -1
        
    def print_info(self):
        self.data.print_info()      
                
# a = neighbor and b = goal using Mantattan Distance formula
def heuristic(a, b):
    # abs(x1−x2)+abs(y1−y2)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])