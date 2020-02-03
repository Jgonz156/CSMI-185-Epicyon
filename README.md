# CSMI-185-Epicyon
Welcome to EPICYON!

How to Play:
1. Run main.py
This will start the game and load a board with both teams ships in oppossing corners!
2. Click the ships
This will bring up the Statistics side bar, displaying important ship values!
NOTE: 
As of this current demo, Buttons at the bottom do not work and can be ignored.
Also, All ships have the same stats, that is not a bug. (This is to be changed later)
3. After clicking on one of your vessels, right-click a Space square.
This will move your ship to that square.
NOTE:
As of this current demo, movement range has not been implemented. This means you can move anywhere on the board.
On par with the honor system, please only right-click tiles directly next to you.
Also, you cannot travel on asteroids.
Be aware that your ship is not duplicating after having right-clicked, 
the tile has not refreshed yet and moving your mouse over it will fix it.
4. After moving within 2 tiles of an enemy, right click them to fire!
This will spend some of your selected ships' ammo to do damage to the other ship selected.
Be aware, friendly fire is active.
NOTE:
As of this current demo, there is no visual or audible feedback to firing.
This means you could be firing without realizing it!
5. Defeat the enemy team in turn-based combat!

CONTROLS:
This game is fully mouse operated so no keyboard input is necessary.
WARNING!!!
Testing with a trackpad has proven that tkinter software doesn't register certain trackpad "Right Mouse Button".
Please play with a dedicated mouse to avoid proprietary software from your computer interfering with game inputs!

CURSOR HOVER (Cursor being placed ontop of tiles):
Your cursor is used to "soft" update the game board with relevant graphics.
For instance, when you move, it may appear as though your ship has duplicated but hovering over the previous tile updates it to a space tile.
What can you CURSOR HOVER?:
1. Space Tiles
2. Ship Tiles
3. Asteroid Tiles
NOTE:
All result in displaing a highlighted version of the same tile.

MOUSE 1 (Left Click):
This button is used to select tiles on screen to update the sidebar with relevant information.
It acts as your selector, so once you've clicked a ship it is ready to use Right Click Actions.
What can you MOUSE 1?:
1. Space Tiles
Results in updating the sidebar with "NO DATA"
2. Ship Tiles
Results in updating the sidebar with relevant ship data
3. Asteroid Tiles
Results in updating the sidebar with "NO DATA"

MOUSE 3 (Right Click):
This button is used to engage actions on ships after you have selected them with left click.
This button is purely used for this function so do not use it for anything else as it may result in unwanted crashes or bugs.
What can you MOUSE 3?:
1. Space Tiles
Results in previously MOUSE 1 selected ship to move to targeted Space Tile
2. Ship Tiles
Results in firing the weapon, spending the ammo, and damaging targeted Ship Tile of previoulsy MOUSE 1 selected Ship Tile
