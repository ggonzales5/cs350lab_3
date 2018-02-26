#Imported modules
import sys
import turtle
import random
from abc import ABCMeta, abstractmethod

#-------------------------------#
# Create an abstract superclass #
# called Cell that enforces the #
# subclasses to implement       #
# specific methods              #
#-------------------------------#
class Cell:

    __metaclass__ = ABCMeta

    @abstractmethod
    def getCoord(self):
        pass

    @abstractmethod
    def getType(self):
        pass

    @abstractmethod
    def getColor(self):
        pass

    @abstractmethod
    def setState(self,val):
        pass
       
    @abstractmethod
    def getState(self):
        pass

    @abstractmethod
    def rules(self,val):
        pass

    @abstractmethod
    def getSurroundingCellState(self,rowcenter=None,colcenter=None):
        pass

#---------------------#
# Radial Cell Class   #
# inherits from the   #
# abstract superclass #
# Cell.               #
#---------------------#
class Radial(Cell):

    #Constructor
    def __init__(self,state,row,col):
     
        self.row = row
        self.col = col
        self.state = state
        
        self.type = "Radial"
        self.color = "green"
        	
    def getCoord(self):
        return (self.row,self.col)

    def getType(self):
        return self.type
    
    def getColor(self):
        return self.color

    def setState(self,val):
        self.state = val
     
    def getState(self):
        return self.state
    
    def rules(self,val):
       
        #Any dead cell with exactly three 
        #live neighbors becomes a live cell
        #Birth a new cell
        if ((val == 3) and (self.state == 0)):
            return 1

        #(Any live cell with two or three live 
        #neighbors lives on to the next generation.)
        #Just keep on living
        elif ((val == 2 or val==3) and (self.state == 1)):  
            return 1

        #Any live cell with fewer than two live 
        #neighbors dies, as if caused by underpopulation.
        #Any live cell with more than three live neighbors 
        #dies, as if by overcrowding.
        #Kill the cell aka. keep it empty
        else:
            return 0
  

    def getSurroundingCellState(self,rowcenter=None,colcenter=None):
 
        # RADIAL CELL
        #
        # x x x
        # x o x
        # x x x

        #Just return the
        #state if every cell.
        return self.state

#---------------------#
# Quad Cell Class     #
# inherits from the   #
# abstract superclass #
# Cell.               #
#---------------------#
class Quad(Cell):

    #Constructor
    def __init__(self,state,row,col):
        
        self.row = row
        self.col = col
        self.state = state
    
        self.type = "Quad"
        self.color = "red"
        
    def getCoord(self):
        return (self.row,self.col)

    def getType(self):
        return self.type

    def getColor(self):
        return self.color

    def setState(self,val):
        self.state = val
      
    def getState(self):
        return self.state

    def rules(self,val):

        #Any alive quad cell with exactly 2 
        #alive neighbors, lives on to next gen.
        if ((val==2) and (self.state==1)):
            return 1
        #Any dead quad cell with one neighbor, 
        #becomes alive.
        elif ((val==1) and (self.state==0)):
            return 1
        #Any alive quad cell with more than 
        #2 alive neighbors, dies.
        elif ((val==3 or val==4) and (self.state==1)):
            return 0
        #Any alive quad cell with less than 
        #2 neighbors, dies.
        elif ((val==1) and (self.state==1)):
            return 0
        #Any dead quad cell with 0,2,3,4 
        #neighbors stays dead
        else:
            return 0

    def getSurroundingCellState(self,rowcenter=None,colcenter=None):
     
        # QUAD CELL
        #
        #   x
        # x o x
        #   x

        #This allows us to look at
        #the LEFT and RIGHT cells 
        # x o x
        if(self.row == rowcenter):
            return self.state

        #This allows us to look at
        #the TOP and BOTTOM cells 
        #  x
        #  o
        #  x  
        elif(self.col == colcenter):
            return self.state
        
        #We dont want the
        #corner cells.
        else:
            return 0

#---------------------#
# Quad Cell Class     #
# inherits from the   #
# abstract superclass #
# Cell.               #
#---------------------#
class Rect(Cell):

    #Constructor
    def __init__(self,state,row,col):
        
        self.row = row
        self.col = col
        self.state = state
    
        self.type = "Rect"
        self.color = "orange"
        
    def getCoord(self):
        return (self.row,self.col)

    def getType(self):
        return self.type
    
    def getColor(self):
        return self.color

    def setState(self,val):
        self.state = val
 
    def getState(self):
        return self.state

    def rules(self,val):

        #Any alive quad cell with exactly 2 
        #alive neighbors, lives on to next gen.
        if ((val==2) and (self.state==1)):
            return 1
        #Any dead quad cell with one neighbor, 
        #becomes alive.
        elif ((val==1) and (self.state==0)):
            return 1
        #Any alive quad cell with more than 
        #2 alive neighbors, dies.
        elif ((val==3 or val==4) and (self.state==1)):
            return 0
        #Any alive quad cell with less than 
        #2 neighbors, dies.
        elif ((val==1) and (self.state==1)):
            return 0
        #Any dead quad cell with 0,2,3,4 
        #neighbors stays dead
        else:
            return 0

    def getSurroundingCellState(self,rowcenter=None,colcenter=None):
     
        # QUADX CELL
        #
        # x   x
        #   o 
        # x   x

        #This allows us to look at
        #only the above cells
        if((self.row != rowcenter) and (self.col != colcenter)):
            return self.state
 
        #We dont want the cross
        #cells.
        else:
            return 0
#---------------------#
# Linear Cell Class   #
# inherits from the   #
# abstract superclass #
# Cell.               #
#---------------------#
class Linear(Cell):

    #Constructor
    def __init__(self,state,row,col):
        
        self.row = row
        self.col = col
        self.state = state
       
        self.type = "Linear"
        self.color = "blue"
        
    def getCoord(self):
        return (self.row,self.col)

    def getType(self):
        return self.type
    
    def getColor(self):
        return self.color

    def setState(self,val):
        self.state = val
               
    def getState(self):
        return self.state

    def rules(self,val):
       
        #Note these rules only apply to LEFT and RIGHT neighbors

        #Any alive linear cell with exactly one alive neighbor, lives on to next gen.
        if ((val==1) and (self.state == 1)):
            return 1
        #Any dead linear cell with one neighbor, becomes alive. BIRTH
        elif ((val==1) and (self.state == 0)):
            return 1 
        #Any alive linear cell with exactly two alive neighbors, dies.
        elif ((val==2) and (self.state == 1)):        
            return 0
        #Any alive linear cell with zero neighbors, dies.
        elif ((val==0) and (self.state == 1)):
            return 0
        #Note that if the cell is dead with two neigbors keep it dead
        #and if the cell is dead with 0 neighbors also keep it dead 
        else:
            return 0
    
    def getSurroundingCellState(self,rowcenter=None,colcenter=None):
     
        # LINEAR CELL
        #
        # x o x

        #We only need to check the row coordanate since we are
        #only looking at the surrounding 8 cells to begin with.
        if(self.row == rowcenter):
            return self.state
        else:
            return 0

#======================#
# CLASS: my Grid class #
# handles primary grid #
# initialization and   # 
# iterative logic.     #
#======================#
class Grid:

    #-------------#
    # Constructor #
    #-------------#
    def __init__(self,cols,rows,cell_pixel_size,cell_obj_types):
        
        self.cols = cols 
        self.rows = rows 
        self.cell_obj_types = cell_obj_types
        self.cell_pixel_size = cell_pixel_size
        
        #Determine the number of cell types we have
        self.num_of_cell_types = len(self.cell_obj_types)

        #Initialize an empty list of lists.
        self.grid_state = [None] * self.cols 
        for i in range(self.cols):
            self.grid_state[i] = [None] * self.rows

    #-------------------------------#
    # Method: create a single cell  #
    # in the grid using the x,y     #
    # coordanates, the cell value,  #
    # and the state value.          #
    #-------------------------------#
    def createCell(self,i,j,state_val,cell_val):
               
        myclassname = self.cell_obj_types[cell_val]
        cell = myclassname(state_val,i,j)
        return cell

    #-----------------------------#
    # Method: Seed the grid by    #
    # filling grid with random    #
    # tuple coords of all three   #
    # types of cells              #
    # ----------------------------#
    def makeRandomMix(self):
        
        #Traverse each cell in the grid
        for i in range(0, self.rows):
            for j in range(0, self.cols):

                #Flip a N sided die to determine 
                #what type of cell to use.
                cell_val = random.randint(0,(self.num_of_cell_types - 1))

                #Flip a coin to determine if
                #alive or dead.
                state_val = random.randint(0,1)
                
                #Store the cell object
                self.grid_state[i][j] = self.createCell(i,j,state_val,cell_val)
                
    #-----------------------------#
    # Method: Seed the grid by    #
    # filling grid with random    #
    # tuple coords of a specified #
    # cell.                       #
    # ----------------------------#
    def makeRandom(self,cell_val):
        
        #Traverse each cell in the grid
        for i in range(0, self.rows):
            for j in range(0, self.cols):

                #Flip a coin to determine if
                #alive or dead.
                state_val = random.randint(0,1)
                 
                #Store the cell object
                self.grid_state[i][j] = self.createCell(i,j,state_val,cell_val)
             
                
    #-----------------------------#
    # Method: Seed the grid by    #
    # filling grid with a list of #
    # tuples                      #
    # ----------------------------#
    def useSeed(self,coord_list,cell_val):

        #Traverse each coordiante and create a cell
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                
                #Seed only the specified
                #coordinates.
                coord_found_flag = 0
                for coord in coord_list:

                    #Add the live seed cell
                    if((i == coord[0]) and (j == coord[1])):

                        #Store the cell object
                        self.grid_state[i][j] = self.createCell(i,j,1,cell_val)
                    
                        coord_found_flag = 1
                        break

                #Add a dead type of the seed 
                #cell if coordanate not in
                #seed list.   
                if coord_found_flag is 0:

                    #Store the cell object
                    self.grid_state[i][j] = self.createCell(i,j,0,cell_val)
              	
    #---------------------------------#
    # Method: calculate a single step #
    # of the simulation               #
    #---------------------------------#
    def step(self):

        '''
        #Just print to console
        for i in range(0, self.rows):     
            for j in range(0, self.cols):
                if self.grid_state[i][j].getState() == 1:
                    print "x",
                else:
                    print ".",
            print ""
        print "\n\n"   
        '''

        #Initialize an empty list of lists as state updates.
        state_updates = [0] * self.cols 
        for i in range(self.cols):
            state_updates[i] = [0] * self.rows

        #Traverse each cell in the grid
        for row in range(0, self.rows):
            
            #Only look at surrounding rows
            v_range = range(max(0, row-1), min(self.rows, row+2))
            
            for col in range(0, self.cols):
                
                sum_val = 0
                
                #Only look at the surrounding 8 cells 
                for hr in range( max(0, col-1), min(self.cols, col+2)):
                    for vr in v_range:

                        sum_val = sum_val + self.grid_state[vr][hr].getSurroundingCellState(row,col)
                
                #Subtract the state of the cell
                #we are looking at.
                sum_val -= self.grid_state[row][col].getState()
                
                #Determine the state of our cell based off
                #of the respective rules of the cell.
                state_updates[row][col] = self.grid_state[row][col].rules(sum_val)

        #Update the entire state all at once using 
        #the new state value
        for row in range(0, self.rows):     
            for col in range(0, self.cols):
                self.grid_state[row][col].setState(state_updates[row][col])


    #----------------------------#
    # Method: Draw all cells     # 
    # on the screen using turtle #
    #----------------------------#
    def display(self):
        
        #Clear the entire display
        turtle.clear()

        #Draw the colored square
        #representing a cell, but
        #remember to change the color
        #for each cell.
        for i in range(0, self.rows):     
            for j in range(0, self.cols):
                if self.grid_state[i][j].getState() is 1:
                    self.draw_square((i,j),self.grid_state[i][j].getColor()) 
        turtle.update()

    #------------------------#
    # Method: Draw a single  #
    # cell on the screen.    #
    #------------------------#                   
    def draw_square(self, coord, color):

        #Pick pen up so we can move to position
        turtle.penup()
        
        #Unpack the coordinate
        x = coord[0]
        y = coord[1]

        #Note since I am using
        #i,jth notation that
        #represents the rows
        #and columns of a list
        #of lists with the origin
        #at the upper left. To
        #display consistently in
        #turtle I need to do a
        #coordanate swap and 
        #shift, which essentially
        #rotates the  graphics by
        #90 degress.
        turtle.setpos(y*self.cell_pixel_size, (self.rows * self.cell_pixel_size) - x*self.cell_pixel_size)
          
        #Set color, and place pen down
        turtle.color(color)
        turtle.pendown()
        turtle.setheading(0)
        turtle.begin_fill()

        #Draw a square and fill it
        for i in range(4):
            turtle.forward(self.cell_pixel_size)
            turtle.left(90)
        turtle.end_fill()

#======================#
# CLASS: my game of    # 
# life class creates   #
# an appropriate sized #
# grid for display     #
# and runs the         #
# simulation.          #
#======================# 
class GameOfLife:

    #-------------#
    # Constructor #
    #-------------#
    def __init__(self,row_cells,col_cells,cell_pixel_size,cell_obj_types):
        
        #Determine screen size, and pixel size
        self.x_screen_size = col_cells * cell_pixel_size
        self.y_screen_size = row_cells * cell_pixel_size
        self.cell_pixel_size = cell_pixel_size

        #Setup turtle screen
        scr = turtle.Screen()
        turtle.mode('standard')
        scr.screensize(self.x_screen_size,self.y_screen_size)
        turtle.setworldcoordinates(0, 0, self.x_screen_size, self.y_screen_size)
        turtle.hideturtle()
        turtle.speed('fastest')
        turtle.tracer(0, 0)
        turtle.penup()

        #Create our Grid object
        self.gol_board = Grid(row_cells, col_cells, self.cell_pixel_size,cell_obj_types)
            

    #-------------------------------#
    # Method: seed the board with a # 
    # particular cell type and      #
    # seed list.                    #
    #-------------------------------#
    def createBoard(self,cell_type=None,seedSet=None):

        if ((seedSet is None) and (cell_type is None)):
            self.gol_board.makeRandomMix()
            self.gol_board.display()
        elif ((seedSet is None) and (cell_type is not None)):
            self.gol_board.makeRandom(cell_type)
            self.gol_board.display() 
        else:
            self.gol_board.useSeed(seedSet,cell_type)
            self.gol_board.display()
    
    #------------------------#
    # Method: allow for      #
    # a pause run simulation #
    #------------------------#
    def pauseRunSimulation(self):

        epoch_count = 0
        while True:
            print("Epoch: %d" % epoch_count)
            raw_input("Press Enter")
            self.gol_board.step()
            self.gol_board.display()
            epoch_count += 1

    #---------------------------#
    # Method: allow for a epoch #
    # bounded simulation.       #
    #---------------------------#
    def epochsRunSimulation(self,epochs):

        epoch_count = 0
        while epoch_count < epochs:
            print("Epoch: %d" % epoch_count)
            self.gol_board.step()
            self.gol_board.display()
            epoch_count += 1


# 0 radial
# 1 linear
# 2 quad
# 3 rect
# Total of 4 different cells


#Seed generation
gol = GameOfLife(40,40,5,[Radial,Linear,Quad,Rect])
gol.createBoard(3,[(0,1),(1,2),(2,0),(2,1),(2,2)])
gol.pauseRunSimulation()

'''
#Random generation
gol = GameOfLife(40,40,5,[Radial,Linear,Quad,Rect])
gol.createBoard()
gol.epochsRunSimulation(100)
'''

'''
#Random generation
gol = GameOfLife(40,40,5,[Radial,Linear,Quad,Rect])
gol.createBoard(3)
gol.pauseRunSimulation()
'''