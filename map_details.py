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

        # Parses through dimensions to find x and y 
        x_len = ""
        y_len = ""
        whiteSpaceCounter = 0

        for w in self.dimensions:
            if (w != " " and whiteSpaceCounter == 0):
                x_len += w
            elif (w != " " and whiteSpaceCounter == 1):
                y_len += w
            else:
                whiteSpaceCounter += 1

        #Splits string into array
        arr = input_matrix.split()

        #Initializes map with 0's
        self.matrix = [[0 for y in range(int(y_len))] for x in range(int(x_len))]

        #Copies over array into 2D map
        x = 0
        y = 0
        try:
            for i in arr:
                if x < int(x_len):
                    if y < int(y_len):
                        self.matrix[x][y] = int(i)
                        y = y + 1
                    else:
                        y = 0
                        x = x + 1
                        self.matrix[x][y] = int(i)
                        y = y + 1
        except Exception as e:
            print(e)
            exit(0)
        



