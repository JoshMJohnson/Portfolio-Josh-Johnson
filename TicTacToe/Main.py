# Tic–Tac–Toe game where the user plays against the AI
# 
# Created By: Josh Johnson

from tkinter import * # used for GUI Interface
import tkinter.messagebox # pop-up message box
import random # random number generation
import time # used for AI delay

# gui settings
window = -1 # gui window
window_width = -1 # width of the gui window

# game details
stop_game = False
begin_game = False
current_player_display = -1
current_player = ''
current_player_symbol_display = -1
current_player_symbol = ''

# player details
player1_symbol = 'X'
player2_symbol = 'O'
player1_name = 'Player One'
player2_name = 'AI'

# game board
states = []
cells = []
playing_board = -1

# adds widgets to the gui
def add_widgets():
    # title display
    title_label = Label(window, text='Tic-Tac-Toe', bg='lightblue', fg='darkblue', relief=RAISED, borderwidth=10, font=('Times', 30, 'bold'))
    title_label.place(anchor=CENTER, relx=.5, rely=.055)

    # current player display
    current_player_label = Label(window, text='Current Player:', bg='lightblue', fg='darkblue', font=('Arial', 10, 'bold'))
    current_player_label.place(x=20, y=85)

    # current player symbol
    current_player_symbol_label = Label(window, text='Current Player Symbol:', bg='lightblue', fg='darkblue', font=('Arial', 10, 'bold'))
    current_player_symbol_label.place(x=310, y=85)

    # bottom menu frame
    bottom_frame = Frame(window, width=window_width, height=100, bg='darkblue')
    bottom_frame.place(in_=window, anchor=CENTER, relx=.5, rely=.92)

    # button dimensions
    button_width = 15
    button_height = 2

    # bottom frame buttons
    Button(bottom_frame, text='Start', width=button_width, height=button_height, command=start_game, bg='lightblue', fg='darkblue', activebackground='lightblue').grid(row=0, column=0, padx=30, pady=15)
    Button(bottom_frame, text='Restart', width=button_width, height=button_height, command=restart_game, bg='lightblue', fg='darkblue', activebackground='lightblue').grid(row=0, column=1)
    Button(bottom_frame, text='Close', width=button_width, height=button_height, command=close_gui, bg='lightblue', fg='darkblue', activebackground='lightblue').grid(row=0, column=2, padx=30)

# creates the gui
def create_gui():
    global window
    window = Tk() # creates window object
    window.title('Tic-Tac-Toe')
    window.geometry('500x700') # width x height
    window.config(bg='lightblue')
    window.resizable(False, False)
    window.update()

    global window_width # begin using the global variable
    window_width = window.winfo_width()

    add_widgets() 
    create_board() 

# creates the tic tac toe board
def create_board():
    # playing board
    playing_board = Frame(window, width=window_width-30, height=150*3, bg='darkblue')
    playing_board.place(in_=window, anchor=CENTER, relx=.5, rely=.5)

    # grid cells
    global cells
    global states

    cells = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    states = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    for x in range(3):
        for y in range(3):
            cells[x][y] = Button(playing_board, width=8, height=4, font=('Sans', 15, 'bold'), relief=RAISED, borderwidth=5, bg='lightblue', fg='darkblue', 
                                activebackground='lightblue', command=lambda xx=x, yy=y : make_move(xx, yy))
            
            if (x == 0 and y == 0) or (x == 2 and y == 2):
                cells[x][y].grid(row=x, column=y, padx=30, pady=30)    
            else:
                cells[x][y].grid(row=x, column=y)

# makes move for player or AI        
def make_move(xx, yy):
    global current_player 
    global current_player_symbol 

    if not begin_game:
        return

    move_made = False

    if current_player == player1_name and states[xx][yy] == 0 and stop_game == False:
        cells[xx][yy].config(text='X')
        states[xx][yy] = 'X'
        move_made = True
        
    if current_player == player2_name and states[xx][yy] == 0 and stop_game == False:
        cells[xx][yy].config(text='O')
        states[xx][yy] = 'O'
        move_made = True
        
    if move_made: # if move has been made
        if not game_over(current_player_symbol): # no winner yet
            if current_player == player1_name:
                current_player = player2_name
                current_player_symbol = player2_symbol
            else:
                current_player = player1_name
                current_player_symbol = player1_symbol

            current_player_display.config(text=current_player)
            current_player_symbol_display.config(text=current_player_symbol)
            window.update()

            if current_player == player2_name:
                ai_move()
        else: # winner
            tkinter.messagebox.showinfo("Winner!", "The winner is: " + current_player)
            for x in range(3):
                for y in range(3):
                    cells[x][y].config(state=DISABLED)

# AI move calculating
def ai_move():
    while True:
        x_value = random.randint(0,2)
        y_value = random.randint(0,2)

        if states[x_value][y_value] == 0:
            time.sleep(random.uniform(0.5,2))
            make_move(x_value, y_value)
            break

# checks to see if there is a winner
def game_over(player_symbol):
    return ((states[0][0] == player_symbol and states[0][1] == player_symbol and states[0][2] == player_symbol) or
            (states[1][0] == player_symbol and states[1][1] == player_symbol and states[1][2] == player_symbol) or
            (states[2][0] == player_symbol and states[2][1] == player_symbol and states[2][2] == player_symbol) or
            (states[0][0] == player_symbol and states[1][0] == player_symbol and states[2][0] == player_symbol) or
            (states[0][1] == player_symbol and states[1][1] == player_symbol and states[2][1] == player_symbol) or
            (states[0][2] == player_symbol and states[1][2] == player_symbol and states[2][2] == player_symbol) or
            (states[0][0] == player_symbol and states[1][1] == player_symbol and states[2][2] == player_symbol) or
            (states[0][2] == player_symbol and states[1][1] == player_symbol and states[2][0] == player_symbol))
        
# starts the game
def start_game():
    global begin_game
    global current_player
    global current_player_display
    global current_player_symbol_display

    if begin_game:
        tkinter.messagebox.showinfo("Start Game", "Game is already started!")
        return

    begin_game = True
    num = random.randint(0,1)

    if num == 1:
        tkinter.messagebox.showinfo("Start Game", "You make the first move!")
        current_player = player1_name
        current_player_symbol = player1_symbol
    else:
        tkinter.messagebox.showinfo("Start Game", "The AI makes the first move!")
        current_player = player2_name
        current_player_symbol = player2_symbol
        
    if current_player_display == -1:
        current_player_display = Label(window, text=current_player, bg='lightblue', fg='darkblue', font=('Arial', 10))
        current_player_display.place(x=125, y=85)
        current_player_symbol_display = Label(window, text=current_player_symbol, bg='lightblue', fg='darkblue', font=('Arial', 10))
        current_player_symbol_display.place(x=465, y=85)
    else:
        current_player_display.config(text=current_player)
        current_player_symbol_display.config(text=current_player_symbol)

    if states != []:
        for x in range(3):
                for y in range(3):
                    cells[x][y].config(state=NORMAL)

    window.update()

    if current_player == player2_name:
        ai_move()

# restarts the game
def restart_game():
    global begin_game

    if not begin_game:
        tkinter.messagebox.showinfo("Restart Game", "Game needs to be started first before you can restart!")
        return

    global current_player
    global current_player_display
    
    begin_game = False
    current_player = ''
    current_player_symbol = ''
    tkinter.messagebox.showinfo("Restart Game", "Game restarted!")

    # clear current player display
    if current_player_display != -1:
        current_player_display.config(text=current_player)
        current_player_symbol_display.config(text=current_player_symbol)

    # clear game board
    global cells
    global states

    for x in range(3):
        for y in range(3):
            if states[x][y] != 0:
                cells[x][y].config(text='')

    states = [
        [0,0,0],
        [0,0,0],
        [0,0,0]
    ]

    start_game()

# terminates the gui
def close_gui():
    window.destroy()

create_gui()
window.mainloop() # infinte loop used to run the application