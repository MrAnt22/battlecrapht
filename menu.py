from tkinter import Frame, Label, Button, PhotoImage, Canvas
from tkinter.ttk import Style
from PIL import Image, ImageTk
from levels.level1 import start_level1
from utils.sounds import play_music, stop_music

def create_menu(root):
    play_music("assets/sounds/human.mp3")
    menu_frame = Frame(root, bg="cyan")
    menu_frame.pack(fill="both", expand=True)

    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    original_image = Image.open("assets/images/menu.jpg")
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

    warcraft_logo = PhotoImage(file="assets/images/logo.png") 
    canvas.create_image(884, 100, image=warcraft_logo)

    start_button_image = PhotoImage(file="assets/images/button_start.png")
    start_button = Button(root,image=start_button_image,command=start_game,borderwidth=0,bg="black")
    canvas.create_window(1384, 300, window=start_button)

    start_button.image = start_button_image
    canvas.warcraft_logo = warcraft_logo

    return menu_frame