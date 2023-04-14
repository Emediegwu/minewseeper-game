from tkinter import Button, Label
import random
import settings
import ctypes
import sys


class Cell:
    cell_count_label_object = None
    cell_count = settings.CELL_COUNT
    all = [] #This stores the cells in a list called 'all'
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.is_opened = False
        self.is_mine_candidate = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        #Append the Cell object to the Cell.all list
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
                location,
                width=8, 
                height=2, 
                )
        btn.bind('<Button-1>', self.left_click_acts) #For left clicks
        btn.bind('<Button-3>', self.right_click_acts) #For right clicks
        self.cell_btn_object = btn

    @staticmethod
    def create_cell_count_label(location):
       labl = Label(
               location, 
               bg="blue", 
               fg="yellow", 
               text=f"Cells left:{Cell.cell_count}", 
               width=12, 
               height=4, 
               font=("Times New Roman", 25)
               )
       Cell.cell_count_label_object = labl

    def left_click_acts(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines_length == 0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()
            
            #If game is completed without clicking mine, this runs:
            if Cell.cell_count == settings.MINES_COUNT:
                #ctypes.windll.user32.MessageBoxW(0, 'Congratulations, you won!', 'YOU WON!', 0)
                print('Congrats! You won the game!')

        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')

    def cell_by_axis(self, x, y):
        #Return cell object based on value of x,y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    
    @property
    def surrounded_cells(self):
        cells = [
            self.cell_by_axis(self.x - 1, self.y - 1),
            self.cell_by_axis(self.x - 1, self.y),
            self.cell_by_axis(self.x - 1, self.y + 1),
            self.cell_by_axis(self.x, self.y - 1),
            self.cell_by_axis(self.x + 1, self.y - 1),
            self.cell_by_axis(self.x + 1, self.y),
            self.cell_by_axis(self.x + 1, self.y + 1),
            self.cell_by_axis(self.x, self.y +1)
            ]

        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surrounded_cells_mines_length(self):
        counter = 0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter += 1

        return counter

    def show_cell(self):
        if not self.is_opened:
            Cell.cell_count -= 1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
            #Replace the text of cell count label with newer count
            if Cell.cell_count_label_object:
                Cell.cell_count_label_object.configure(
                        text=f"Cells left:{Cell.cell_count}"
                        )
            #To return right-clicked cell to white after marking it as a mine cell
            self.cell_btn_object.configure(bg='white')

        # Check to see that cells are opened after function is run
        self.is_opened = True

    def show_mine(self):
        # To interrupt game and display loss message if mine is clicked
        self.cell_btn_object.configure(bg='red')

        # The code below is commented out because windll is a Windows version
        # What it does is to display a pop up box to the user saying that game is over, when a mine is clicked
        #ctypes.windll.user32.MessageBoxW(0, 'You clicked on a mine', 'Game over!', 0)
        print('You clicked on a mine. Game over.')
        sys.exit() #Exits game if mine is clicked

    def right_click_acts(self, event):
        if not self.is_mine_candidate:
            self.cell_btn_object.configure(
                    bg='purple')
            self.is_mine_candidate = True
        else:
            self.cell_btn_object.configure(
                    bg='white')
            self.is_mine_candidate = False

    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
                Cell.all, settings.MINES_COUNT
                ) #The .sample method in the random module takes 2 args, 1st the list that contains all, and
                 #then the number of randomized items we want (9)
        for picked_cell in picked_cells:
            picked_cell.is_mine = True
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
