from tkinter import *
import settings
import utilities
from cell import Cell

#Change window settings:
root = Tk()
root.configure(bg="black") #Changes window background colour to black, bg for background
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}') #This sets Tkinter's  window size, origins from settings.py
root.title("My Minesweeper Game") #This changes the game title in the title bar
root.resizable(False, False) #This sets the Tkinter window stable and makes it unresizable,
                            # with 2 False elements, one for WIDTH an the other for HEIGHT

top_frame = Frame(
        root,
        bg='black',
        width=settings.WIDTH,
        height=utilities.height_pcent(25) #Original height divided by 4, as determined by utilities.py
        )

top_frame.place(x=0, y=0)

game_title = Label(
        top_frame, 
        bg='black', 
        fg='white', 
        text='Minesweeper Game', 
        font=('Times New Roman', 48)
        )

game_title.place(x=utilities.width_pcent(25), y=0)


left_frame = Frame(
        root,
        bg='black',
        width=utilities.width_pcent(25), #25% of original width, determined by utilities.py
        height=utilities.height_pcent(75) #75% of original height, as determined by utilities.py
        )

left_frame.place(x=0, y=utilities.height_pcent(25))

centre_frame = Frame(
        root,
        bg='grey',
        width=utilities.width_pcent(75), #75% of original width, determined by utilities.py
        height=utilities.height_pcent(75) #75% of original height, as determined by utilities.py
        )

centre_frame.place(x=utilities.width_pcent(25), y=utilities.height_pcent(25))


'''
#An alternative way of coding rows and columns by arranging them individually, as
#opposed to the below method

c1 = Cell()
c1.create_btn_object(centre_frame)
c1.cell_btn_object.grid(column=0, row=0)

c2 = Cell()
c2.create_btn_object(centre_frame)
c2.cell_btn_object.grid(column=0, row=1)

#c3 = Cell() ...and so on
'''


#Arranging rows and columns

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(centre_frame)
        c.cell_btn_object.grid(column=x, row=y)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)

Cell.randomize_mines()

#Run/call window
root.mainloop()
