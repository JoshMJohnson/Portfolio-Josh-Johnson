# Tic–Tac–Toe game where the user plays against the AI or another human player
# 
# Created By: Josh Johnson

from tkinter import * # used for GUI Interface
import tkinter.messagebox # pop-up message box
import random # random number generation
import time # used for AI delay

# gui settings
window = -1 # main gui window
window_width = -1 # width of the gui window
opponent_window = -1 # opponent select window

# game details
begin_game = False
is_tie = False
current_player_display = -1
current_player = ''
current_player_symbol_display = -1
current_player_symbol = ''

# player details
player1_symbol = 'X'
player2_symbol = 'O'
player1_name = 'Player One'
player2_name = 'Player Two'
opponent_ai = -1 # 1 if AI and 0 if human player 

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
    Button(bottom_frame, text='Start', cursor="circle", width=button_width, height=button_height, command=ready_game, bg='lightblue', fg='darkblue', activebackground='lightblue').grid(row=0, column=0, padx=30, pady=15)
    Button(bottom_frame, text='Restart', cursor="circle", width=button_width, height=button_height, command=restart_game, bg='lightblue', fg='darkblue', activebackground='lightblue').grid(row=0, column=1)
    Button(bottom_frame, text='Close', cursor="circle", width=button_width, height=button_height, command=close_gui, bg='lightblue', fg='darkblue', activebackground='lightblue').grid(row=0, column=2, padx=30)

# creates the main gui containing the board
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

# creates the tic-tac-toe board
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
            cells[x][y] = Button(playing_board, cursor="target", width=8, height=4, font=('Sans', 15, 'bold'), relief=RAISED, borderwidth=5, bg='lightblue', fg='darkblue', 
                                activebackground='lightblue', command=lambda xx=x, yy=y : make_move(xx, yy))
            
            if (x == 0 and y == 0) or (x == 2 and y == 2):
                cells[x][y].grid(row=x, column=y, padx=30, pady=30)    
            else:
                cells[x][y].grid(row=x, column=y, padx=(4, 4))

# registers when a move has been made      
def make_move(xx, yy):
    global current_player 
    global current_player_symbol 

    if not begin_game:
        return

    move_made = False

    if current_player == player1_name and states[xx][yy] == 0:
        cells[xx][yy].config(text='X')
        states[xx][yy] = 'X'
        move_made = True
        
    if current_player == player2_name and states[xx][yy] == 0:
        cells[xx][yy].config(text='O')
        states[xx][yy] = 'O'
        move_made = True
        
    if move_made: # if move has been made
        if not game_over(current_player_symbol) and not is_tie: # no winner yet
            if current_player == player1_name:
                current_player = player2_name
                current_player_symbol = player2_symbol
            else:
                current_player = player1_name
                current_player_symbol = player1_symbol

            current_player_display.config(text=current_player)
            current_player_symbol_display.config(text=current_player_symbol)
            window.update()

            if current_player == player2_name and opponent_ai == 1:
                ai_move()
        elif is_tie:
            tkinter.messagebox.showinfo("Game Over!", "It was a tie")
            for x in range(3):
                for y in range(3):
                    cells[x][y].config(state=DISABLED)
        else: # winner
            tkinter.messagebox.showinfo("Game Over!", "The winner is: " + current_player)
            for x in range(3):
                for y in range(3):
                    cells[x][y].config(state=DISABLED)

# AI move calculations
def ai_move():
    while True:
        x_value = random.randint(0,2)
        y_value = random.randint(0,2)

        if states[x_value][y_value] == 0:
            time.sleep(random.uniform(0.5,2))
            make_move(x_value, y_value)
            break

# choose opponent to be the AI or another human player
def choose_opponent():
    window.withdraw() # makes game window invisible

    global opponent_window
    opponent_window = Tk() # creates window object
    opponent_window.title('Tic-Tac-Toe')
    opponent_window.geometry('290x250') # width x height
    opponent_window.config(bg='lightblue')
    opponent_window.resizable(False, False)

    # opponent options label
    opponent_label = Label(opponent_window, text='Choose Opponent', bg='lightblue', fg='darkblue', relief=RAISED, borderwidth=10, font=('Times', 20, 'bold'))
    opponent_label.place(anchor=CENTER, relx=.5, rely=.15)
    
    # opponent options frame
    opponent_frame = Frame(opponent_window, width=opponent_window.winfo_width(), height=100, bg='darkblue')
    opponent_frame.place(in_=opponent_window, anchor=CENTER, relx=.5, rely=.60)

    # button dimensions
    button_width = 10
    button_height = 5

    # opponent option buttons
    Button(opponent_frame, cursor="circle", text='AI', width=button_width, height=button_height, bg='lightblue', fg='darkblue', relief=RAISED, activebackground='lightblue', command=lambda : opponent_setup(True)).grid(row=0, column=0, padx=(23,15), pady=30)
    Button(opponent_frame, cursor="circle", text='Human', width=button_width, height=button_height, bg='lightblue', fg='darkblue', relief=RAISED, activebackground='lightblue', command=lambda : opponent_setup(False)).grid(row=0, column=1, padx=(15, 23), pady=30)

    opponent_window.update()

# sets up game for oppenent
def opponent_setup(is_opponent_ai):
    global player2_name
    global opponent_ai
    global begin_game

    if is_opponent_ai:
        player2_name = 'AI'
        opponent_ai = 1
    else:
        player2_name = 'Player Two'
        opponent_ai = 0  

    window.deiconify() # makes game window visible again
    opponent_window.destroy() # remove the choose opponent window
    begin_game = True
    start_game()

# checks to see if there is a winner or a tie
def game_over(player_symbol):
    global is_tie
    is_tie = True

    for x in range(3):
        for y in range(3):
            if states[x][y] == 0:
                is_tie = False 
                break

        if not is_tie:
            break

    game_won = ((states[0][0] == player_symbol and states[0][1] == player_symbol and states[0][2] == player_symbol) or
                (states[1][0] == player_symbol and states[1][1] == player_symbol and states[1][2] == player_symbol) or
                (states[2][0] == player_symbol and states[2][1] == player_symbol and states[2][2] == player_symbol) or
                (states[0][0] == player_symbol and states[1][0] == player_symbol and states[2][0] == player_symbol) or
                (states[0][1] == player_symbol and states[1][1] == player_symbol and states[2][1] == player_symbol) or
                (states[0][2] == player_symbol and states[1][2] == player_symbol and states[2][2] == player_symbol) or
                (states[0][0] == player_symbol and states[1][1] == player_symbol and states[2][2] == player_symbol) or
                (states[0][2] == player_symbol and states[1][1] == player_symbol and states[2][0] == player_symbol))

    if game_won:
        is_tie = False

    return game_won

# player indicated that they want to start a game
def ready_game():
    if begin_game:
        tkinter.messagebox.showinfo("Start Game", "Game is already started!")
        return    

    choose_opponent()
        
# prepares the game to be played and makes first move if playing against the AI
def start_game():
    global current_player
    global current_player_display
    global current_player_symbol_display

    starting_player = random.randint(0,1)

    if starting_player == 0:
        if opponent_ai == 1:
            tkinter.messagebox.showinfo("Start Game", "You make the first move!")
        else:
            tkinter.messagebox.showinfo("Start Game", "Player 1 makes the first move!")

        current_player = player1_name
        current_player_symbol = player1_symbol
    else:
        if opponent_ai == 1:
            tkinter.messagebox.showinfo("Start Game", "The AI makes the first move!")
        else:
            tkinter.messagebox.showinfo("Start Game", "Player 2 makes the first move!")

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

    if current_player == player2_name and opponent_ai == 1:
        ai_move()

# restart the game
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

    ready_game()

# terminates the main gui
def close_gui():
    window.destroy()

create_gui()
window.mainloop() # infinte loop used to run the application