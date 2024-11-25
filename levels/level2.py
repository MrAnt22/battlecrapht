from PIL import Image, ImageTk
import tkinter as tk
import random

root = tk.Tk()

# Define constants
GRID_SIZE = 5  # Size of the grid (5x5)
CELL_SIZE = 100  # Size of each cell in pixels
MOVEMENT_POINTS = 5  # Movement points per turn

# Function to resize images
def resize_image(file_path, size):
    img = Image.open(file_path)
    img = img.resize((size, size), Image.Resampling.LANCZOS)  # Use LANCZOS for high-quality resizing
    return ImageTk.PhotoImage(img)

# Load and resize images
CELL_SIZE = 64  # Example cell size
hero_image = resize_image("assets/images/arthas.png", CELL_SIZE)
enemy_image = resize_image("assets/images/snake.png", CELL_SIZE)
treasure_image = resize_image("assets/images/treasure.png", CELL_SIZE)

# Initialize the map grid
map_grid = [
    ["grass", "treasure", "enemy", "grass", "mountain"],
    ["grass", "grass", "grass", "grass", "grass"],
    ["resource", "grass", "hero", "enemy", "grass"],
    ["grass", "water", "water", "grass", "treasure"],
    ["grass", "grass", "grass", "grass", "grass"]
]

# Initialize the hero
class Hero:
    def __init__(self, x, y, movement_points):
        self.x = x
        self.y = y
        self.movement_points = movement_points
        self.health = 100

    def move(self, direction):
        if self.movement_points > 0:
            if direction == "up" and self.y > 0 and map_grid[self.y - 1][self.x] != "mountain":
                self.y -= 1
            elif direction == "down" and self.y < GRID_SIZE - 1 and map_grid[self.y + 1][self.x] != "mountain":
                self.y += 1
            elif direction == "left" and self.x > 0 and map_grid[self.y][self.x - 1] != "mountain":
                self.x -= 1
            elif direction == "right" and self.x < GRID_SIZE - 1 and map_grid[self.y][self.x + 1] != "mountain":
                self.x += 1
            else:
                return
            self.movement_points -= 1
            interact_with_tile()

# Initialize the enemy
class Enemy:
    def __init__(self, health):
        self.health = health

hero = Hero(2, 2, MOVEMENT_POINTS)
enemy = Enemy(50)

# Tkinter setup
root.title("Heroes of Might and Magic III - Simplified")

canvas = tk.Canvas(root, width=GRID_SIZE * CELL_SIZE, height=GRID_SIZE * CELL_SIZE)
canvas.pack()

# Draw the grid and map elements
def draw_map():
    canvas.delete("all")
    for y in range(GRID_SIZE):
        for x in range(GRID_SIZE):
            cell = map_grid[y][x]
            # Draw terrain
            color = "green" if cell in ["grass", "resource"] else "blue" if cell == "water" else "gray"
            canvas.create_rectangle(x * CELL_SIZE, y * CELL_SIZE, 
                                    (x + 1) * CELL_SIZE, (y + 1) * CELL_SIZE, fill=color)
            # Draw objects
            if cell == "hero":
                canvas.create_image(x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2, image=hero_image)
            elif cell == "enemy":
                canvas.create_image(x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2, image=enemy_image)
            elif cell == "treasure":
                canvas.create_image(x * CELL_SIZE + CELL_SIZE // 2, y * CELL_SIZE + CELL_SIZE // 2, image=treasure_image)

# Interact with the tile
def interact_with_tile():
    global enemy
    cell = map_grid[hero.y][hero.x]
    if cell == "treasure":
        print("You found a treasure!")
        map_grid[hero.y][hero.x] = "grass"  # Remove the treasure
    elif cell == "enemy":
        print("An enemy appears!")
        start_combat()
    elif cell == "resource":
        print("You gathered resources!")
        map_grid[hero.y][hero.x] = "grass"  # Remove the resource
    draw_map()

# Combat system
def start_combat():
    global enemy
    print("Combat begins!")
    while enemy.health > 0 and hero.health > 0:
        # Hero attacks
        enemy.health -= 10
        print(f"Enemy health: {enemy.health}")
        if enemy.health <= 0:
            print("You defeated the enemy!")
            map_grid[hero.y][hero.x] = "grass"  # Remove enemy from map
            break
        # Enemy attacks
        hero.health -= 5
        print(f"Hero health: {hero.health}")
        if hero.health <= 0:
            print("You were defeated!")
            break
    draw_map()

# Movement
def on_key_press(event):
    if event.keysym == "Up":
        hero.move("up")
    elif event.keysym == "Down":
        hero.move("down")
    elif event.keysym == "Left":
        hero.move("left")
    elif event.keysym == "Right":
        hero.move("right")
    draw_map()

# Bind keys
root.bind("<KeyPress>", on_key_press)  

# Start game
draw_map()
root.mainloop()
