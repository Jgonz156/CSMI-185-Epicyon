"""
File: weapons.py
Team: Wengel, Julian, Garrett
Description: Defines and creates all the weapons in the game
"""

# Weapon object, used by ships to damage other ships
class Weapon():
    def __init__(self, damage, ammo, can_damage_shields, can_damage_health, name):
        self.damage = damage #Some number
        self.ammo = ammo #Some number
        self.cds = can_damage_shields #Some boolean
        self.cdh = can_damage_health #Some boolean
        self.name = name #Some string

# All weapons in game
weapon_library = {}
small_cannon = Weapon(5, 20, False, True, "Small Cannon")
weapon_library["small_cannon"] = small_cannon
big_cannon = Weapon(20, 5, False, True, "Big Cannon")
weapon_library["big_cannon"] = big_cannon
small_laser = Weapon(5, 20, True, False, "Small Laser")
weapon_library["small_laser"] = small_laser
big_laser = Weapon(20, 5, True, False, "Big Laser")
weapon_library["big_laser"] = big_laser
