from tkinter import Canvas, Frame, Label, PhotoImage
from PIL import Image, ImageTk
from characters.arthas import Arthas
from characters.snake import Snake
from utils.sounds import play_music, play_random_sound
from utils.loggers import FileLogger, ConsoleLogger, MultiLogger
import random

def start_level1(root):


    #
    file_logger = FileLogger("game_logs.txt")
    console_logger = ConsoleLogger()
    logger = MultiLogger(file_logger, console_logger)
    logger.log("info", "Level 1 initialized.")
    #


    play_music("assets/sounds/ithas.mp3")
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    w = screen_width
    h = screen_height
    game_time = 60
    remaining_time = game_time
    game_frame = Frame(root, bg="black")
    game_frame.pack(fill="both", expand=True)


    bg1 = PhotoImage(file="assets/images/lordaeron.png")
    arthas_image = PhotoImage(file="assets/images/arthas.png")
    snake_image = PhotoImage(file="assets/images/snake.png")
    metal_image = PhotoImage(file="assets/images/metal.png")

    game_frame.bg_image = bg1
    game_frame.arthas_image = arthas_image
    game_frame.snake_image = snake_image
    game_frame.metal_image = metal_image

    original_image = Image.open("assets/images/lordaeron.png")
    stretched_image = original_image.resize((screen_width, screen_height))
    bg1 = ImageTk.PhotoImage(stretched_image)

    canvas = Canvas(game_frame, width=screen_width, height=screen_height)
    canvas.pack(expand=True, fill="both")
    canvas.create_image(0, 0, image=bg1, anchor="nw")
    canvas.bg_image = bg1

    score = 0
    arthas = Arthas(canvas, arthas_image)
    snake = Snake(canvas, snake_image)

    score_label = Label(root, text="Score: 0", bg="white", fg="red", font="Arial 14 bold")
    canvas.create_window(100, 50, window=score_label)

    timer_label = Label(
        root, text=f"Time Remaining: {remaining_time} seconds", bg="white", fg="blue", font="Arial 14 bold"
    )
    canvas.create_window(w - 150, 50, window=timer_label)
    def update_timer():
        nonlocal remaining_time
        if remaining_time > 0:
            remaining_time -= 1
            timer_label.config(text=f"Time Remaining: {remaining_time} seconds")
            root.after(1000, update_timer)  # Call this function again after 1 second
        else:
            game_over_timeout()
    def game_over_timeout():
        canvas.create_text(w // 2,h // 2,text="Time's up! Game Over!",font="Arial 24 bold",fill="red")
        #
        logger.log("info", "Game Over due to timeout.")
        #
        root.unbind("<Left>")
        root.unbind("<Right>")
        root.unbind("<Up>")
        root.unbind("<Down>")
        root.unbind("<space>")
        root.after(3000, root.quit)

    update_timer()
    
    def update_score():
        nonlocal score
        score += 1
        score_label.config(text=f"Score: {score}")
        snake.respawn()
        play_random_sound()
        snake_attack()
        snake.update_health(damage = 5)
        if score == 20:
            win()

    def on_collision():
        if arthas.collides_with(snake):

            #
            logger.log("debug", f"Collision detected at Arthas ({arthas.x}, {arthas.y}).")
            #

            update_score()

    is_stunned = False
    stun_message_id = None
    attack_object_id = None
    def snake_attack():
        nonlocal is_stunned, stun_message_id, attack_object_id
        if score == 15:
            is_stunned = True

            random_x = random.randint(100, w - 100)
            random_y = random.randint(100, h - 100)

            attack_object_id = canvas.create_image(random_x, random_y, image=metal_image)

            stun_message_id = canvas.create_text(
                w // 2, 100, text="Click on metal gear from metal gear solid V to destroy him!", font="Arial 18 bold", fill="white"
            )

            def on_click(event):
                nonlocal is_stunned, stun_message_id, attack_object_id
                if attack_object_id is not None:
                    coords = canvas.coords(attack_object_id)
                    if coords and len(coords) >= 2:
                        image_width = 100
                        if coords[0] - image_width / 2 <= event.x <= coords[0] + image_width / 2 and \
                        coords[1] - image_width / 2 <= event.y <= coords[1] + image_width / 2:
                            canvas.delete(attack_object_id)
                            canvas.delete(stun_message_id)
                            stun_message_id = None
                            attack_object_id = None
                            is_stunned = False
                    
            canvas.bind("<Button-1>", on_click)
            root.after(4000, lambda: game_over() if is_stunned else None)

        elif score % 5 == 0 and score != 0 and score != 15 and score != 20 :
            if not is_stunned:
                is_stunned = True
                stun_message_id = canvas.create_text(w // 2, h // 2, text="Arthas is stunned by coward Snake! Press the left mouse button to keep fighting!", font="Arial 14", fill="red")
                root.bind("<Button-1>", release_stun)

    def release_stun(event):
        nonlocal is_stunned, stun_message_id
        is_stunned = False
        if stun_message_id:
            canvas.delete(attack_object_id)
            canvas.delete(stun_message_id)
            stun_message_id = None
        root.unbind("<Button-1>")
    
    def game_over():
            nonlocal is_stunned
            if is_stunned:

                #
                logger.log("info", "Game Over triggered.")
                #

                canvas.create_text(
                    w // 2,
                    h // 2,
                    text="Game Over! You failed to defeat the attack!",
                    font="Arial 24 bold",
                    fill="red",
                )
                root.unbind("<Button-1>")
                root.after(3000, root.quit)
            
    def win():

        #
        logger.log("info", "Game over triggered")
        #

        canvas.create_text(
            w // 2,
            h // 2,
            text="You defeated the Solid Snake!",
            font="Arial 24 bold",
            fill="red",
        )
        root.unbind("<Left>")
        root.unbind("<Right>")
        root.unbind("<Up>")
        root.unbind("<Down>")
        root.unbind("<space>")
        root.after(3000, root.quit)

    def move_left():
        global last_direction
        if arthas.x > 0 and not is_stunned:
            arthas.move(-10, 0)
            last_direction = {"x": -1, "y": 0}
            on_collision()

    def move_right():
        global last_direction
        if arthas.x < w and not is_stunned:
            arthas.move(10, 0)
            last_direction = {"x": 1, "y": 0}
            on_collision()

    def move_up():
        global last_direction
        if arthas.y > 0 and not is_stunned:
            arthas.move(0, -10)
            last_direction = {"x": 0, "y": -1}
            on_collision()

    def move_down():
        global last_direction
        if arthas.y < h and not is_stunned:
            arthas.move(0, 10)
            last_direction = {"x": 0, "y": 1}
            on_collision()
    can_dash = True

    can_dash = True

    def dash(event):
        nonlocal can_dash
        if can_dash and not is_stunned:
            can_dash = False
            dash_distance = 300
            dx = last_direction["x"] * dash_distance
            dy = last_direction["y"] * dash_distance

            new_x = arthas.x + dx
            new_y = arthas.y + dy
            if 0 <= new_x <= w and 0 <= new_y <= h:
                arthas.move(dx, dy)

            def reset_dash():
                nonlocal can_dash
                can_dash = True

            root.after(1000, reset_dash)

            #
        else: logger.log("error", "Failed to dash")
            #
            
    root.bind("<Left>", lambda event: move_left())
    root.bind("<Right>",lambda event: move_right())
    root.bind("<Up>",lambda event: move_up())
    root.bind("<Down>",lambda event: move_down())
    root.bind("<space>", dash)