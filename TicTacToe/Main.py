# Tic–Tac–Toe game where the user plays against the program
# 
# Created By: Josh Johnson

from tkinter import * # used for GUI Interface

window_width = -1 # window width dimension

# adds widgets to the gui
def add_widgets(window):
    # bottom menu frame
    bottom_frame = Frame(window, width=window_width, height=100, bg='darkblue')
    bottom_frame.place(in_=window, anchor=CENTER, relx=.5, rely=.9)

    # button dimensions
    button_width = 15
    button_height = 2

    # bottom frame buttons
    Button(bottom_frame, text='Start', width=button_width, height=button_height, command=start_game, bg='lightblue', fg='darkblue', activebackground='lightblue').grid(row=0, column=0, padx=30, pady=15)
    Button(bottom_frame, text='Restart', width=button_width, height=button_height, command=restart_game, bg='lightblue', fg='darkblue', activebackground='lightblue').grid(row=0, column=1)
    Button(bottom_frame, text='Close', width=button_width, height=button_height, command=close_gui, bg='lightblue', fg='darkblue', activebackground='lightblue').grid(row=0, column=2, padx=30, pady=15)

# creates the gui
def create_gui():
    window = Tk() # creates window object
    window.title('Tic-Tac-Toe')
    window.geometry('500x600') # width x height
    window.config(bg='lightblue')
    window.resizable(False, False)
    window.update()

    global window_width # begin using the global variable
    window_width = window.winfo_width()

    add_widgets(window)

    return window

# starts the game
def start_game():
    return

# restarts the game
def restart_game():
    return

# terminates the gui
def close_gui():
    window.destroy()

# creates the tic tac toe board
def create_board(window):
    # playing board
    playing_board = Frame(window, width=window_width-30, height=150*3, bg='darkblue')
    playing_board.place(in_=window, x=15, y=15)

    



window = create_gui()
create_board(window) # creates playing board
window.mainloop() # infinte loop used to run the application