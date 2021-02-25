f = open("map.txt")

extract_details = 4

dimensions = 0
starting_loc = 0
goal = 0

matrix = 0

#Reads first three lines
for i in range(extract_details):
    if i == 0:
        dimensions = f.readline()    
    elif i == 1:
        starting_loc = f.readline()
    elif i == 2:
        goal = f.readline()
    else:
        matrix = f.read()

y_len = int(dimensions[2])
x_len = int(dimensions[0])
    
# print(dimensions)
# print(starting_loc)
# print(goal)

#Splits string into array
arr = matrix.split()
print(arr)

#Initializes map with 0's
map = [[0 for y in range(y_len)] for x in range(x_len)]

#Copies over array into 2D map
x = 0
y = 0
for i in arr:
    if x < x_len:
        if y < y_len:
            map[x][y] = i
            y = y + 1
        else:
            y = 0
            x = x + 1
            map[x][y] = i
            y = y + 1
            
print(map)
