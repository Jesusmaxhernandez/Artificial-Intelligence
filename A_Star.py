import Node

# Code from https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2
def astar(maze, start, end):   

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
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            
            return path[::-1] # Return reversed path

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
    end = (4, 3)

    path = astar(inMatrix, start, end)
    print(path)


if __name__ == '__main__':
    main()