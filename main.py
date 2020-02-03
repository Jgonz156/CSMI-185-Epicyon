"""
File: main.py
Team: Wengel, Julian, Garrett
Description: Game
"""

import tkinter as tk # the Tkinter Module
from tkinterframe import * # Game board file
from sidebar import * # Interaction menu file
from weapons import * # Weapon class and library file
from ships import * # Ship class and library file
from space import * # Space tile class file

# Needs to be integrated with code below in debug game
class Epicyon():
    def __init__(self):
        #self.space = space
        self.game_state = "off"

    def start_game(self): # Method that begins the game, acts as an on switch
        self.game_state = "on"

    def stop_game(self): # Method that ends the game, acts as an off switch
        self.game_state = "off"

#debug game

travel_key = 0

if travel_key == 0:
    def refresher(event):
        create_sidebar(side_frame, 0)

d_g = Epicyon()
d_g.start_game()

if d_g.game_state == "on":
    game = tk.Tk() # Game window

    # Game frame that holds sidebar and game board
    game_frame = tk.LabelFrame(game, text = "Untitled Space Game") 
    game_frame.grid(row=1,column=1)
    if travel_key == 0:
        game.bind("<Button-1>", refresher)

    # Frame that holds the game board imported from tkinterframe.py
    board_frame = tk.Label(game_frame)
    board_frame.grid(row=1,column=1)
    create_game_board(board_frame, 0)

    # Frame that holds the side bar imported from sidebar.py
    side_frame = tk.Label(game_frame)
    side_frame.grid(row=1,column=2)
# Runs the full, integrated game
game.mainloop()