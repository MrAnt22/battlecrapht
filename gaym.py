from tkinter import *
import random
import pygame
import random


root = Tk()

root.title("Ратмира ігрове вікно")
root.geometry("1000x800")
root.configure(bg="#D5BA33")
root.maxsize(1000, 800)

pygame.mixer.init()
music1 = pygame.mixer.Sound("music/ithas.mp3")
music1.set_volume(0.1)
music1.play()

bg1 = PhotoImage(file="lordaeron.png")

art = PhotoImage(file="arthas.png", width=200, height=228)
krl = PhotoImage(file="snake.png", width=103, height=200)

arthas_replics = ["arthasreplics/1.mp3", "arthasreplics/2.mp3", "arthasreplics/3.mp3", "arthasreplics/4.mp3",
                    "arthasreplics/5.mp3", "arthasreplics/6.mp3", "arthasreplics/7.mp3", "arthasreplics/8.mp3",
                    "arthasreplics/9.mp3", "arthasreplics/10.mp3", "arthasreplics/11.mp3", "arthasreplics/12.mp3"]

w, h = 1000, 720
orig_canva = Canvas(root, height=h, width=w)
orig_canva.pack(expand=True, fill="both")
orig_canva.create_image(0,0, image=bg1,anchor = "nw")

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

def play_random_sound():
    sound_file = random.choice(arthas_replics)
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.1)

score = 0
def score_upd():
    global score
    score += 1
    scr.config(text = "Score: {}".format(score))
    snake_attack()
scr = Label(root,text="Score: 0", bg="white", fg="red",width=100,height=30, font="aerial 14")
scr.pack()


is_stunned = False
stun_message_id = None
def snake_attack():
    global is_stunned, stun_message_id
    if score % 5 == 0 and score != 0:
        if not is_stunned:
            is_stunned = True
            stun_message_id = orig_canva.create_text(w // 2, h // 2, text="Arthas is stunned by coward Snake! Press the left mouse button to keep fighting!", font="Arial 14", fill="red")
            root.bind("<Button-1>", release_stun)
def release_stun(event):
    global is_stunned, stun_message_id
    is_stunned = False
    if stun_message_id:
        orig_canva.delete(stun_message_id)
        stun_message_id = None
    root.unbind("<Button-1>")


def left(event):
    if arthas.x > 0 and not is_stunned:
        arthas.move(-10, 0)
        hit()
def right(event):
    if arthas.x < w and not is_stunned:
        arthas.move(10, 0)
        hit()
def up(event):
    if arthas.y > 0 and not is_stunned:
        arthas.move(0, -10)
        hit()
def down(event):
    if arthas.y < h and not is_stunned:
        arthas.move(0, 10)
        hit()
def hit():
    
    arthas_hitbox = orig_canva.bbox(arthas.hitbox)
    snake_hitbox = orig_canva.bbox(snake.hitbox)
    if (arthas_hitbox[2] > snake_hitbox[0] and
        arthas_hitbox[0] < snake_hitbox[2] and
        arthas_hitbox[3] > snake_hitbox[1] and
        arthas_hitbox[1] < snake_hitbox[3]):
        play_random_sound()
        snake.respawn()
        score_upd()


root.bind("<Left>", left)
root.bind("<Right>", right)
root.bind("<Up>", up)
root.bind("<Down>", down)

root.mainloop()
