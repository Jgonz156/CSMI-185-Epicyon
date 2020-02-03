"""
File: ships.py
Team: Wengel, Julian, Garrett
Description: This file defines and creates all the ships in the game
"""

import random as r
from tkinterframe import *
from weapons import *

# Ship object, the main game's units/ships
class Ship():
    def __init__(self, armor, shield, health, Weapon, move_range):
        self.armor = armor #Some number
        self.shield = shield #Some number
        self.health = health #Some number
        self.weapon = Weapon #Some Weapon object (potentially tuple of objects)
        self.mr = move_range #Some number

    def damage_shields(self, enemy): # Method that allows for shield damage on enemy ships
        if self.weapon.cds == True:
            enemy.shield -= self.weapon.damage
            self.weapon.ammo -= 1
        else: # Placeholder, Game does not require console
            print("Our Cannon Can't Damage Their Shields!")

    def damage_health(self, enemy): # Method that allows for health damage on enemy ships
        if self.weapon.cdh == True:
            enemy.health -= (self.weapon.damage - enemy.armor)
            self.weapon.ammo -= 1
        else: # Placeholder, Game does not require console
            print("Our Laser Can't Damage Their Hull!")

    def move(self, target_standing, current_standing): 
        target_standing.become_ship(self)
        print(target_standing)
        current_standing.become_standing()
        print(current_standing)

# All ship objects in game
ship_library = {}
ship_library["rand_ship_1"] = Ship(r.randint(0,5), r.randint(0,50), r.randint(0,100), weapon_library[r.choice(list(weapon_library.keys()))], r.randint(1,3))
ship_library["rand_ship_2"] = Ship(r.randint(0,5), r.randint(0,50), r.randint(0,100), weapon_library[r.choice(list(weapon_library.keys()))], r.randint(1,3))
ship_library["rand_ship_3"] = Ship(r.randint(0,5), r.randint(0,50), r.randint(0,100), weapon_library[r.choice(list(weapon_library.keys()))], r.randint(1,3))
ship_library["rand_ship_4"] = Ship(r.randint(0,5), r.randint(0,50), r.randint(0,100), weapon_library[r.choice(list(weapon_library.keys()))], r.randint(1,3))
ship_library["rand_ship_5"] = Ship(r.randint(0,5), r.randint(0,50), r.randint(0,100), weapon_library[r.choice(list(weapon_library.keys()))], r.randint(1,3))
ship_library["rand_ship_6"] = Ship(r.randint(0,5), r.randint(0,50), r.randint(0,100), weapon_library[r.choice(list(weapon_library.keys()))], r.randint(1,3))
ship_library["rand_ship_7"] = Ship(r.randint(0,5), r.randint(0,50), r.randint(0,100), weapon_library[r.choice(list(weapon_library.keys()))], r.randint(1,3))
ship_library["rand_ship_8"] = Ship(r.randint(0,5), r.randint(0,50), r.randint(0,100), weapon_library[r.choice(list(weapon_library.keys()))], r.randint(1,3))
ship_library["rand_ship_9"] = Ship(r.randint(0,5), r.randint(0,50), r.randint(0,100), weapon_library[r.choice(list(weapon_library.keys()))], r.randint(1,3))
ship_library["rand_ship_10"] = Ship(r.randint(0,5), r.randint(0,50), r.randint(0,100), weapon_library[r.choice(list(weapon_library.keys()))], r.randint(1,3))
ship_library["rand_ship_11"] = Ship(r.randint(0,5), r.randint(0,50), r.randint(0,100), weapon_library[r.choice(list(weapon_library.keys()))], r.randint(1,3))
ship_library["rand_ship_12"] = Ship(r.randint(0,5), r.randint(0,50), r.randint(0,100), weapon_library[r.choice(list(weapon_library.keys()))], r.randint(1,3))