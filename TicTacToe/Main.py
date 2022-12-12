# Tic–Tac–Toe game where the user plays against the program
# 
# Created By: Josh Johnson

from tkinter import * # used for GUI Interface

# adds widgets to the gui
def add_widgets(window):
    # window dimensions
    window_width = window.winfo_width()
    window_height = window.winfo_height()

    # bottom menu frame
    bottom_frame = Frame(window, width=window_width, height=100, bg="darkblue")
    bottom_frame.place(in_=window, anchor="c", relx=.5, rely=.9)

    # button dimensions
    button_width = 15
    button_height = 2

    # bottom frame buttons
    Button(bottom_frame, text='Start', width=button_width, height=button_height, command=start_game, bg="lightblue", fg="darkblue").grid(row=0, column=0, padx=30, pady=15)
    Button(bottom_frame, text='Restart', width=button_width, height=button_height, command=restart_game, bg="lightblue", fg="darkblue").grid(row=0, column=1)
    Button(bottom_frame, text='Close', width=button_width, height=button_height, command=close_gui, bg="lightblue", fg="darkblue").grid(row=0, column=2, padx=30, pady=15)

# creates the gui
def create_gui():
    window = Tk() # creates window object
    window.title('Tic-Tac-Toe')
    window.geometry("500x600") # width x height
    window.config(bg="lightblue")
    window.resizable(False, False)
    window.update()

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

window = create_gui()
window.mainloop() # infinte loop used to run the application