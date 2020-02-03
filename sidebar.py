"""
File: sidebar.py
Team: Wengel, Julian, Garrett
Description: This file creates the sidebar for user interaction
"""
import tkinter as tk
import tkinterframe as gb
from weapons import * # Weapon class and library file
from ships import * # Ship class and library file
from space import * # Space tile class file

target_data = None
standing_data = None
travel_key = 0

def create_sidebar(frame, debug_input):
    frame_passer = frame
    debug_passer = debug_input
    def final_sidebar(frame, pulse_data, debug_input):
        if debug_input == 1:
            window = tk.Tk()

            window.title("Statistics Game")

            # window.configure(background='black')

        if debug_input == 0:
            window = frame

        # creates "Statistics" title
        title = tk.Label(window, text="Statistics", font="courier 20 bold", fg="black")
        title.grid(row=1, column=2)
        # title.configure(background='black')

        # creates "Ship Type Statistics" subtitle
        subheading = tk.Label(window, text="Ship Type Statistics", font="none 10 italic", fg="darkred")
        subheading.grid(row=2, column=2)
        # subheading.configure(background='black')

        # creates "Armor" category
        armor_t = tk.Label(window, text="Armor: ", font="courier 15 bold", fg="black")
        armor_t.grid(row=3, column=1)
        # armor_t.configure(background='black')

        # updates text with statistics
        try:
            armorval = tk.Label(window, text=pulse_data.ship.armor, fg="black")
        except AttributeError:
            armorval = tk.Label(window, text="No data", fg="white")
        armorval.grid(row=3, column=2)
        # armorval.configure(background='black')

        # creates "Armor" category
        shield_t = tk.Label(window, text="Shield: ", font="courier 15 bold", fg="black")
        shield_t.grid(row=4, column=1)
        # shield_t.configure(background='black')

        # updates text with statistics
        try:
            shieldval = tk.Label(window, text=pulse_data.ship.shield, fg="black")
        except AttributeError:
            shieldval = tk.Label(window, text="No data", fg="black")
        shieldval.grid(row=4, column=2)
        # shieldval.configure(background='black')

        # creates "Health" category
        health_t = tk.Label(window, text="Health: ", font="courier 15 bold", fg="black")
        health_t.grid(row=5, column=1)
        # health_t.configure(background='black')

        # updates text with statistics
        try:
            healthval = tk.Label(window, text=pulse_data.ship.health, fg="black")
        except AttributeError:
            healthval = tk.Label(window, text="No data", fg="white")
        healthval.grid(row=5, column=2)
        # healthval.configure(background='black')

        # creates "Damage" category
        damage_t = tk.Label(window, text="Damage: ", font="courier 15 bold", fg="black")
        damage_t.grid(row=6, column=1)
        # damage_t.configure(background='black')

        # updates text with statistics
        try:
            damageval = tk.Label(window, text=pulse_data.ship.weapon.damage, fg="black")
        except AttributeError:
            damageval = tk.Label(window, text="No data", fg="black")
        damageval.grid(row=6, column=2)
        # damageval.configure(background='black')

        # weapon1 = tk.Label(window, text="Weapon 1")
        # weapon1.grid(row=8, column=1)

        # weapon2 = tk.Label(window, text="Weapon 2")
        # weapon2.grid(row=8, column=2)

        # fire1 = tk.Label(window, text="FIRE")
        # fire1.grid(row=9, column=1)

        # def button_pressed():
        #     print("You pressed fire!")

        # creates button for "Weapon" 

        fireButton1 = tk.LabelFrame(window, text="Weapon")
        fireButton1.grid(row=10, column=2)
        fireButton1.configure(background='blue')

        # updates values with type of weapon
        fire1 = tk.Label(fireButton1, text=pulse_data.ship.weapon.name)
        fire1.grid(row=1, column=1)
        # fireButton1['command'] = button_pressed


         # creates button for "Ammo" 
        fireButton2 = tk.LabelFrame(window, text="Ammo")
        fireButton2.grid(row=10, column=3)
        fireButton2.configure(background='blue')

        def printo(event):
            print(gb.pulse_data)
            print(pulse_data)

        # updates values with type of ammo
        fire2 = tk.Label(fireButton2, text=pulse_data.ship.weapon.ammo)
        fire2.bind("<Button-1>", printo)
        fire2.grid(row=1, column=1)
        if debug_input == 1:
            window.mainloop()
    final_sidebar(frame_passer, gb.pulse_data, debug_passer)
def main():
    pass

if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   create_sidebar(None, 1)
   main()