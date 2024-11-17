from tkinter import Frame, Label, Button
from levels.level1 import start_level1
from utils.sounds import play_music, stop_music

def create_menu(root):
    play_music("assets/sounds/human.mp3")
    menu_frame = Frame(root, bg="cyan")
    menu_frame.pack(fill="both", expand=True)

    def start_game():
        stop_music()
        menu_frame.pack_forget()
        start_level1(root)

    def quit_game():
        root.quit()

    Label(menu_frame, text="Welcome our honoured guest!", font=("Arial", 24), bg="lightblue").pack(pady=20)
    Button(menu_frame, text="Start Game", command=start_game, font=("Arial", 18), bg="green", fg="white").pack(pady=10)
    Button(menu_frame, text="Quit", command=quit_game, font=("Arial", 18), bg="red", fg="white").pack(pady=10)

    return menu_frame
