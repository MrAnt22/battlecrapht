from tkinter import Frame, Label, Button, PhotoImage, Canvas
from PIL import Image, ImageTk
from levels.level1 import start_level1
from utils.sounds import play_music, stop_music

def create_menu(root):
    play_music("assets/sounds/human.mp3")
    menu_frame = Frame(root, bg="cyan")
    menu_frame.pack(fill="both", expand=True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    original_image = Image.open("assets/images/menu.png")
    stretched_image = original_image.resize((screen_width, screen_height))
    menubg = ImageTk.PhotoImage(stretched_image)

    canvas = Canvas(menu_frame, width=screen_width, height=screen_height)
    canvas.pack(expand=True, fill="both")
    canvas.create_image(0, 0, image=menubg, anchor="nw")
    canvas.bg_image = menubg

    def start_game():
        stop_music()
        menu_frame.pack_forget()
        start_level1(root)

    def quit_game():
        root.quit()

    canvas.create_text(400, 50, text="Warcraft IV", font=("Arial", 64), fill="Dark green")
    start_button = Button(root, text="Start Game", command=start_game, font=("Arial", 18), bg="green", fg="white")
    quit_button = Button(root, text="Quit", command=quit_game, font=("Arial", 18), bg="red", fg="white")

    
    canvas.create_window(200, 300, window=start_button)
    canvas.create_window(200, 400, window=quit_button)

    return menu_frame
