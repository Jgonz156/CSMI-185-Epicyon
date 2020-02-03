"""
File: weapons.py
Team: Wengel, Julian, Garrett
Description: Defines and creates the tile objects the ships move between
"""

import random
from tkinterframe import *

# Space object (synonomous with term "tile")
class Space():
    def __init__(self, tkinter_id):
        self.id = tkinter_id # Some Canvas PhotoImage id
        self.ship = None # Some object
        self.standing = False # Some Bool/obj
        self.rock = False # Some Bool (Potentially obj in future)

    # Tag definer methods
    def become_ship(self, ship): # Assigns ship tag with ship object
        self.standing = False
        self.rock = False
        self.ship = ship

    def become_standing(self, tile): # Assigns space/standing tag
        self.ship = None
        self.rock = False
        self.standing = tile
        
    def become_rock(self): # Assigns asteroid tag
        self.rock = True
        self.standing = False
        self.ship = None

    # Un-used random tile generator for game board generator in tkinter.py
    def rand_contructor(self):
        random.choice([self.become_rock(), self.become_ship(random.choice(weapon_library)), self.become_standing()])
