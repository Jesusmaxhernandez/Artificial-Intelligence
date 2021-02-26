class Map:

    def __init__(self):     
        self.dimensions = 0
        self.starting_loc = 0
        self.goal = 0
        self.matrix = 0
    
    def __dimensions__(self):
        return self.dimensions

    def __starting_loc__(self):
        return self.starting_loc
    
    def __goal__(self):
        return self.goal
    
    def __matrix__(self):
        return self.matrix
    
    def read_file(self,f):
        extract_details = 4

        #Reads first three lines
        for i in range(extract_details):
            if i == 0:
                self.dimensions = f.readline()    
            elif i == 1:
                self.starting_loc = f.readline()
            elif i == 2:
                self.goal = f.readline()
            else:
                input_matrix = f.read()

        y_len = int(self.dimensions[2])
        x_len = int(self.dimensions[0])

        #Splits string into array
        arr = input_matrix.split()

        #Initializes map with 0's
        self.matrix = [[0 for y in range(y_len)] for x in range(x_len)]

        #Copies over array into 2D map
        x = 0
        y = 0
        for i in arr:
            if x < x_len:
                if y < y_len:
                    self.matrix[x][y] = int(i)
                    y = y + 1
                else:
                    y = 0
                    x = x + 1
                    self.matrix[x][y] = int(i)
                    y = y + 1
        



