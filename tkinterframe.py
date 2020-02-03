"""
File: tkinterframe.py
Team: Wengel, Julian, Garrett
Description: Creates game board
"""

import tkinter as tk
import random
from sidebar import *
from space import *
from ships import *
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image # Import Photo Image Library to process .png and .jpg files

pulse_data = None # Temporary store variable for holding object data

# Stores Key as canvas id and value as object
red_ship_dict = {} # Stores red ships 
blue_ship_dict = {} # Store blue ships
rock_dict = {} # Stores asteroids
stand_dict = {} # Stores space tiles

target_data = None # Temporary store variable for holding object data when firing weapons

# Defines data collection from clicking on a game board tile
def id_pulse(event):
    global pulse_data
    print(pulse_data)
    id = event.widget.find_closest(event.x, event.y)[0] # Id of tile clicked

    # Id dictionary filter. assigns pulse data value of tile object clicked
    if id in blue_ship_dict:
        pulse_data = blue_ship_dict[id]
    elif id in red_ship_dict:
        pulse_data = red_ship_dict[id]
    elif id in stand_dict:
        pulse_data = None
    elif id in rock_dict:
        pulse_data = None

# Game board creator (used by main.py to create the game board)
def create_game_board(frame, debug_input): #frame is a tkinter frame passed in main.py and debug_input allows tkinter.py to run sperate from main

    canvas = Canvas()
    if debug_input == 0: # Allows main.py to assign the game board to it's game frame
        canvas = Canvas(frame)
    canvas.config(width=450, height=600)
    canvas.pack()
        
    # Imports image files to display object tiles
    # Note: all images denoted with h in the beginning are the image displayed when hovering over a tile with your mouse
    space_jpg = ImageTk.PhotoImage(file = "space.jpg")
    h_space_jpg = ImageTk.PhotoImage(file = "highlightedspace.jpg")

    blue_ship = ImageTk.PhotoImage(file = "blueship.png")
    h_blue_ship = ImageTk.PhotoImage(file = "highlightedblueship.png")

    red_ship = ImageTk.PhotoImage(file = "redship.png")
    h_red_ship = ImageTk.PhotoImage(file = "highlightedredship.png")

    asteroid = ImageTk.PhotoImage(file = "asteroid.png")
    h_asteroid = ImageTk.PhotoImage(file = "highlightedasteroid.png")

    # Defines how a ship is locked onto and fired at by another ship
    def firing_data(event):
        global pulse_data
        id_2 = event.widget.find_closest(event.x, event.y)[0] 
        your_ship = pulse_data # Your ship (The ship you just left-clicked on)
        enemy_ship = id_2 # Enemy ship (The ship you just right-clicked on after left-clicking your ship)

        # Enemy ship object grabber (Pulls object from ship library to have one object edit another with Ship class methods)
        try:
            target_data = red_ship_dict[enemy_ship]
        except KeyError:
            pass
        try:
            target_data = blue_ship_dict[enemy_ship]
        except KeyError:
            pass

        # Weapon damage filter (Only allows laser to hit shields and cannons to hit health)
        if your_ship.ship.weapon.cds == True:
            your_ship.ship.damage_shields(target_data.ship)

        if your_ship.ship.weapon.cdh == True:
            your_ship.ship.damage_health(target_data.ship)

        # Ship killer (Defines how a ship dies and turns into a space tile)
        if target_data.ship.health <= 0:
            create_standing(target_data)
            try:
                red_ship_dict.pop(target_data.id)
            except KeyError:
                pass
            try:
                blue_ship_dict.pop(target_data.id)
            except KeyError:
                pass

    # Defines how a ship moves (It is really just the 2 tiles swapping location on the board)
    def move_data(event):
        print(3)
        global pulse_data
        id_1 = event.widget.find_closest(event.x, event.y)[0]
        target_data = stand_dict[id_1] # Where you are moving (The space tile you right clicked on)
        ship_data = pulse_data # The ship you are moving (The ship tile you left clicked on prior to right-clicking)
        #pulse_data.ship.move(target_data, pulse_data)
        
        # Ship mover for red ships
        if pulse_data.id in red_ship_dict: # Ship filter (This is to grab the correct data from the correct ship dictionary)
            create_red_ship(target_data) # Creates an identical ship on the space tile
            red_ship_dict.pop(pulse_data.id) # Removes ship from dictionary (This is because the dictionary key is storing the inccorect canvas id)

        # Ship mover for blue ships
        if pulse_data.id in blue_ship_dict: 
            create_blue_ship(target_data)
            blue_ship_dict.pop(pulse_data.id)

        # Space tile mover
        if id_1 in stand_dict:
            create_standing(ship_data) # Creates a new space tile in place of ship's old location
            stand_dict.pop(id_1) # Removes old space tile from dictionary (This is because the dictionary key is storing the inccorect canvas id)

    # Defines how the game board tile picture is changed to the highlighted version
    def tilehighlight(event):
        id = event.widget.find_closest(event.x, event.y)[0] # Tile your mouse is over

        # Tile filter (filters id to change to correct unique highlighted image [Otherwise they all turn into one image])
        if id in rock_dict:
            canvas.itemconfig(event.widget.find_closest(event.x, event.y), image=h_asteroid) # Change to highlighted asteroid image
        elif id in red_ship_dict:
            canvas.itemconfig(event.widget.find_closest(event.x, event.y), image=h_red_ship) # Change to highlighted red ship image
        elif id in blue_ship_dict:
            canvas.itemconfig(event.widget.find_closest(event.x, event.y), image=h_blue_ship) # Change to highlighted blue ship image
        elif id in stand_dict:
            canvas.itemconfig(event.widget.find_closest(event.x, event.y), image=h_space_jpg) # Change to highlighted space tile image

    # Defines how the game board tile picture is changed back to the unhighlighted version
    def unhighlight(event):
        id = event.widget.find_closest(event.x, event.y)[0]
        if id in rock_dict:
            canvas.itemconfig(event.widget.find_closest(event.x, event.y), image=asteroid)
        elif id in red_ship_dict:
            canvas.itemconfig(event.widget.find_closest(event.x, event.y), image=red_ship)
        elif id in blue_ship_dict:
            canvas.itemconfig(event.widget.find_closest(event.x, event.y), image=blue_ship)
        elif id in stand_dict:
            canvas.itemconfig(event.widget.find_closest(event.x, event.y), image=space_jpg)

    # Defines how a red ship tile and red ship object are created
    # Note: Used by the game generator [the for loops at the bottom] to initially create red ships on game start and ship movement
    def create_red_ship(standing_location):
        # Filter used to sort between when initially creating a ship and moving a ship
        if standing_location == None: # When NOT moving (This is the initial creation at the start of the game)
            id = canvas.create_image(75*row, 75*column, anchor= NW, image=red_ship) # Creates unique canvas id
            ship = Space(id) # Creates space object (class found in space.py) 
            ship.become_ship(ship_library[random.choice(list(ship_library.keys()))]) # Random ship assigner (gets ships from ships.py) also assigns space object with ship tag
            red_ship_dict[id] = ship # Places ship in red ship dictionary
            rect_list.append(id) # Adds new canvas id to a debug list

            # Ship function attacher (binds ship functions to ship canvas id)
            canvas.tag_bind(id, "<Enter>", tilehighlight) # Binds tile highlight to mouse hover
            canvas.tag_bind(id, "<Leave>", unhighlight) # Binds tile highlight to mouse hover
            canvas.tag_bind(id, "<Button-1>", id_pulse) # Binds pulse data to left click
            canvas.tag_bind(id, "<Button-3>", firing_data) # Binds firing ability to ship
        else: # When moving a ship
            ship = standing_location
            ship.become_ship(pulse_data.ship) # Takes passed space tile (Space object with standing tag) and changes Space objects tag to ship
            red_ship_dict[ship.id] = ship # Places ship back into ship library with new canvas id
            canvas.tag_bind(ship.id, "<Enter>", tilehighlight)
            canvas.tag_bind(ship.id, "<Leave>", unhighlight)
            canvas.tag_bind(ship.id, "<Button-1>", id_pulse)
            canvas.tag_bind(ship.id, "<Button-3>", firing_data)

    # Same as prior but for blue ships
    def create_blue_ship(standing_location):
        if standing_location == None:
            id = canvas.create_image(75*row, 75*column, anchor= NW, image=blue_ship)
            ship = Space(id)
            ship.become_ship(ship_library[random.choice(list(ship_library.keys()))])
            blue_ship_dict[id] = ship
            rect_list.append(id)
            canvas.tag_bind(id, "<Enter>", tilehighlight)
            canvas.tag_bind(id, "<Leave>", unhighlight)
            canvas.tag_bind(id, "<Button-1>", id_pulse)
            canvas.tag_bind(id, "<Button-3>", firing_data)
        else:
            ship = standing_location
            ship.become_ship(pulse_data.ship)
            blue_ship_dict[ship.id] = ship
            canvas.tag_bind(ship.id, "<Enter>", tilehighlight)
            canvas.tag_bind(ship.id, "<Leave>", unhighlight)
            canvas.tag_bind(ship.id, "<Button-1>", id_pulse)
            canvas.tag_bind(ship.id, "<Button-3>", firing_data)

    # Defines how to create an asteroid tile and asteroid object
    # Note: Used by the game generator [the for loops at the bottom] to initially create asteroids on game start
    def create_rock():
        id = canvas.create_image(75*row, 75*column, anchor= NW, image=asteroid) # Creates unique canvas id
        rock = Space(id) # Creates a Space object
        rock.become_rock() # Assigns asteroid tag on space object
        rock_dict[id] = rock # Adds asteroid to asteroid library
        rect_list.append(id) # Adds canvas id to debug library

        # Attaches asteroid functions
        canvas.tag_bind(id, "<Enter>", tilehighlight)
        canvas.tag_bind(id, "<Leave>", unhighlight)
        canvas.tag_bind(id, "<Button-1>", id_pulse)

    # Defines how to create a space tile
    # Note: Used by the game generator [the for loops at the bottom] to initially create space tiles on game start and ship movement
    def create_standing(ship_location):
        if ship_location == None: # When NOT moving
            id = canvas.create_image(75*row, 75*column, anchor= NW, image=space_jpg) # Creates unqiue canvas id
            space = Space(id) # Creates new space object
            space.become_standing(None) # Assigns space object with space tile tag
            stand_dict[id] = space # Puts space tile in space tile dictionary
            rect_list.append(id) # Adds canvas id to debug list

            # Space tile function attacher
            canvas.tag_bind(id, "<Button-3>", move_data)
            canvas.tag_bind(id, "<Enter>", tilehighlight)
            canvas.tag_bind(id, "<Leave>", unhighlight)
            canvas.tag_bind(id, "<Button-1>", id_pulse)
        else: # When moving a space tile
            space = ship_location
            stand_dict[space.id] = space # Places new space tile into space dictionary
            space.become_standing(space) # Takes passed ship tile (Space object with ship tag) and changes Space objects tag to standing
            canvas.tag_bind(space.id, "<Button-3>", move_data)
            canvas.tag_bind(space.id, "<Enter>", tilehighlight)
            canvas.tag_bind(space.id, "<Leave>", unhighlight)
            canvas.tag_bind(space.id, "<Button-1>", id_pulse)

    rect_list = [] # Debug list

    # Game board (initial start) generator
    counter = 0
    for row in range(0, 6):
        for column in range(0, 8):
            if counter in [32, 40, 41]: # Filter that makes red ship tiles
                create_red_ship(None)

            elif counter in [6, 7, 15]: # Filter that makes blue ship tiles
                create_blue_ship(None)

            elif random.randint(0,5) == 2: # Filter that has a 1 in 5 chance to create an asteroid tiles
                create_rock()

            else: # Filter than turns the rest of the tiles into non-unique space tiles
                create_standing(None)

            counter+=1

    if debug_input == 1: # Allows for tkinter.py to run
        canvas.mainloop()

def main():
    pass

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   create_game_board(None, 1)
   main()
