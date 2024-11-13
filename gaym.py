from tkinter import *
import random

root = Tk()

root.title("Ратмира ігрове вікно")
root.minsize(240, 255)
root.geometry("1000x800")
root.configure(bg="#D5BA33")
root.maxsize(1000, 800)

art = PhotoImage(file="C:/Users/maksl/Desktop/redfolder/arthas.png", width=200, height=228)
krl = PhotoImage(file="C:/Users/maksl/Desktop/redfolder/snake.png", width=103, height=200)

w, h = 1000, 720
orig_canva = Canvas(root, height=h, width=w, bg="black")
orig_canva.pack()

class Arthas:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = w // 2
        self.y = h // 2
        self.image_id = self.canvas.create_image(self.x, self.y, image=art)
        self.hitbox = self.canvas.create_rectangle(self.x,self.y, self.x+20, self.y+20,outline="", fill="")
    
    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.canvas.move(self.image_id, dx, dy)
        self.canvas.move(self.hitbox, dx, dy)

class Snake:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.randint(0, (1000 // 50) - 1) * 50
        self.y = random.randint(0, (800 // 50) - 1) * 50
        self.image_id = canvas.create_image(self.x, self.y, image=krl)
        self.hitbox = canvas.create_rectangle(self.x-10,self.y-40, self.x+70, self.y+70, fill="", outline="")

    def respawn(self):

        self.x = random.randint(0, (1000 // 50) - 1) * 50
        self.y = random.randint(0, (800 // 50) - 1) * 50
        self.canvas.coords(self.image_id, self.x, self.y)
        self.canvas.coords(self.hitbox, self.x - 10, self.y - 40, self.x + 70, self.y + 70)

arthas = Arthas(orig_canva)
snake = Snake(orig_canva)

score = 0

def score_upd():
    global score
    score += 1
    scr.config(text = "Score: {}".format(score))

scr = Label(root,text="Score: 0", bg="white", fg="red",width=100,height=30, font="aerial 14")
scr.pack()

def left(event):
    if arthas.x > 0:
        arthas.move(-10, 0)
        hit()
def right(event):
    if arthas.x < w:
        arthas.move(10, 0)
        hit()
def up(event):
    if arthas.y > 0:
        arthas.move(0, -10)
        hit()
def down(event):
    if arthas.y < h:
        arthas.move(0, 10)
        hit()
def hit():
    arthas_hitbox = orig_canva.bbox(arthas.hitbox)
    snake_hitbox = orig_canva.bbox(snake.hitbox)
    if (arthas_hitbox[2] > snake_hitbox[0] and
        arthas_hitbox[0] < snake_hitbox[2] and
        arthas_hitbox[3] > snake_hitbox[1] and
        arthas_hitbox[1] < snake_hitbox[3]):
        print("nice!")
        snake.respawn()
        score_upd()

root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()
