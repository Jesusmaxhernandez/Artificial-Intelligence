import Node
from timeit import default_timer as timer

# Code from https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
class A_Star():
    def __init__(self):
        self.costPath = 0 
        self.numNodesExp = 0
        self.maxNodesMem = 0
        self.time = 0
        self.pathSeq = []

    def __costPath__(self):
        return self.costPath

    def __numNodesExp__(self):
        return self.numNodesExp
    
    def __maxNodeMem__(self):
        return self.maxNodesInMem
    
    def __time__(self):
        return self.time
    
    def __pathSeq__(self):
        return self.pathSeq

    def astar(self, maze, start, end):   
        #Timer Start
        timerStart = timer()
        queue = [(start, [])]

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
            if timer() - timerStart >= 180:
                print("BFS elapsed time is greater than 3 minutes ")
                exit()

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
                #End the timer
                timerEnd = timer()
                totalTime = (timerEnd - timerStart) * 1000
               
                path = []
                current = current_node
                while current is not None:
                    path.append(current.position)
                    current = current.parent
                
                self.costPath = findTotalCost(path, maze)
                self.pathSeq = path[::-1] 
                return 1 #path[::-1] # Return reversed path

            # Generate children
            children = []
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
                for closed_child in closed_list:
                    if child == closed_child:
                        continue
                # Initilize two parameters for heuristic (manhattan Distance)
                neighbors = child.position[0],child.position[1]
                goalNode = end_node.position[0],end_node.position[1]
                
                # Create the f, g, and h values
                child.g = current_node.g + 1
                child.h = heuristic(neighbors, goalNode)  
                child.f = child.g + child.h

                # Child is already in the open list
                for open_node in open_list:
                    if child == open_node and child.g > open_node.g:
                        continue

                # Add the child to the open list
                open_list.append(child)

                # Increment number of nodes expanded
                self.numNodesExp += 1
                

def heuristic(a, b):#a = neighbor and b = goal // Need to fix?
        return abs(a[0] - b[0]) + abs(a[1] - b[1])#Manhattan Distance

def findTotalCost(path, matrix):

    totalC = 0
    for node in path:
        totalC += matrix[node[0]][node[1]]

    return totalC

def main():

    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    og = [[2,4,2,1,4,5,2], 
                [0,1,2,3,5,3,1], 
                [2,0,4,4,1,2,4], 
                [2,5,5,3,2,0,1], 
                [4,3,3,2,1,0,1]]
    
    inMatrix = [[2,4,2,1,4,5,2], 
                [0,1,2,3,5,3,1], 
                [2,0,0,0,0,0,4], 
                [2,5,5,3,2,0,1], 
                [4,3,3,2,1,1,1]]
    start = (1, 2)
    end = (0, 0)

    path = A_Star()
    path.astar(inMatrix, start, end)
    print(path.pathSeq)
    print(path.costPath)
    print(path.numNodesExp)


if __name__ == '__main__':
    main()