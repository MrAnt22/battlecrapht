import random

class Snake:
    def __init__(self, canvas, image):  
        self.canvas = canvas
        self.health = 100
        self.max_health = 100
        self.x = random.randint(0, canvas.winfo_width() // 50) * 50
        self.y = random.randint(0, canvas.winfo_height() // 50) * 50
        self.image_id = canvas.create_image(self.x, self.y, image=image)
        self.hitbox = canvas.create_rectangle(self.x - 10, self.y - 40, self.x + 70, self.y + 70, fill="", outline="")
        canvas_width = self.canvas.winfo_width()
        self.health_bar_outline = canvas.create_rectangle(20, 20, canvas_width - 20, 40, outline="black")
        self.health_bar_fill = canvas.create_rectangle(20, 20, 20 + (canvas_width - 40), 40, fill="green")


    def respawn(self):
        self.x = random.randint(0, self.canvas.winfo_width() // 50) * 50
        self.y = random.randint(0, self.canvas.winfo_height() // 50) * 50
        self.canvas.coords(self.image_id, self.x, self.y)
        self.canvas.coords(self.hitbox, self.x - 10, self.y - 40, self.x + 70, self.y + 70)

    def update_health(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

        health_percentage = self.health / self.max_health
        canvas_width = self.canvas.winfo_width()
        bar_width = (canvas_width - 40) * health_percentage
        self.canvas.coords(self.health_bar_fill,20, 20, 20 + bar_width, 40)

        if health_percentage > 0.6:
            self.canvas.itemconfig(self.health_bar_fill, fill="green")
        elif health_percentage > 0.3:
            self.canvas.itemconfig(self.health_bar_fill, fill="yellow")
        else:
            self.canvas.itemconfig(self.health_bar_fill, fill="red")