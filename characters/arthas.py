class Arthas:
    def __init__(self, canvas, image):
        self.canvas = canvas
        self.x = canvas.winfo_width() // 2
        self.y = canvas.winfo_height() // 2
        self.image_id = self.canvas.create_image(self.x, self.y, image=image)
        self.hitbox = self.canvas.create_rectangle(self.x, self.y, self.x + 20, self.y + 20, outline="", fill="")

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        self.canvas.move(self.image_id, dx, dy)
        self.canvas.move(self.hitbox, dx, dy)

    def collides_with(self, other):
        arthas_bbox = self.canvas.bbox(self.hitbox)
        other_bbox = self.canvas.bbox(other.hitbox)
        return (arthas_bbox[2] > other_bbox[0] and
                arthas_bbox[0] < other_bbox[2] and
                arthas_bbox[3] > other_bbox[1] and
                arthas_bbox[1] < other_bbox[3])
