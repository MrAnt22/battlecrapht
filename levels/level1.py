from tkinter import Canvas, Frame, Label, PhotoImage
from characters.arthas import Arthas
from characters.snake import Snake
from utils.sounds import play_random_sound, play_music

def start_level1(root):
    play_music("assets/sounds/ithas.mp3")
    w, h = 1000, 720
    game_frame = Frame(root, bg="black")
    game_frame.pack(fill="both", expand=True)

    bg1 = PhotoImage(file="assets/images/lordaeron.png")
    arthas_image = PhotoImage(file="assets/images/arthas.png")
    snake_image = PhotoImage(file="assets/images/snake.png")

    game_frame.bg_image = bg1
    game_frame.arthas_image = arthas_image
    game_frame.snake_image = snake_image

    canvas = Canvas(game_frame, height=h, width=w)
    canvas.pack(expand=True, fill="both")
    canvas.create_image(0, 0, image=bg1, anchor="nw")

    score = 0
    arthas = Arthas(canvas, arthas_image)
    snake = Snake(canvas, snake_image)

    score_label = Label(game_frame, text=f"Score: {score}", bg="white", fg="red", font="Arial 14")
    score_label.pack()

    def update_score():
        nonlocal score
        score += 1
        score_label.config(text=f"Score: {score}")
        snake.respawn()
        play_random_sound()
        snake_attack()

    def on_collision():
        if arthas.collides_with(snake):
            update_score()

    is_stunned = False
    stun_message_id = None
    def snake_attack():
        nonlocal is_stunned, stun_message_id
        if score % 5 == 0 and score != 0:
            if not is_stunned:
                is_stunned = True
                stun_message_id = canvas.create_text(w // 2, h // 2, text="Arthas is stunned by coward Snake! Press the left mouse button to keep fighting!", font="Arial 14", fill="red")
                root.bind("<Button-1>", release_stun)
    def release_stun(event):
        nonlocal is_stunned, stun_message_id
        is_stunned = False
        if stun_message_id:
            canvas.delete(stun_message_id)
            stun_message_id = None
        root.unbind("<Button-1>")
    
    def left(event):
        if arthas.x > 0 and not is_stunned:
            arthas.move(-10, 0)
            on_collision()
    def right(event):
        if arthas.x < w and not is_stunned:
            arthas.move(10, 0)
            on_collision()
    def up(event):
        if arthas.y > 0 and not is_stunned:
            arthas.move(0, -10)
            on_collision()
    def down(event):
        if arthas.y < h and not is_stunned:
            arthas.move(0, 10)
            on_collision()
            
    root.bind("<Left>", left)
    root.bind("<Right>", right)
    root.bind("<Up>", up)
    root.bind("<Down>", down)
