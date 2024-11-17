import random

class Snake:
    def __init__(self, canvas, image):
        self.canvas = canvas
        self.x = random.randint(0, canvas.winfo_width() // 50) * 50
        self.y = random.randint(0, canvas.winfo_height() // 50) * 50
        self.image_id = canvas.create_image(self.x, self.y, image=image)
        self.hitbox = canvas.create_rectangle(self.x - 10, self.y - 40, self.x + 70, self.y + 70, fill="", outline="")

    def respawn(self):
        self.x = random.randint(0, self.canvas.winfo_width() // 50) * 50
        self.y = random.randint(0, self.canvas.winfo_height() // 50) * 50
        self.canvas.coords(self.image_id, self.x, self.y)
        self.canvas.coords(self.hitbox, self.x - 10, self.y - 40, self.x + 70, self.y + 70)
