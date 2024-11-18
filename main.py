from tkinter import Tk, Frame
from menu import create_menu
from utils.sounds import initialize_sounds


root = Tk()
root.title("Ратмира ігрове вікно")
root.geometry("1000x800")
root.configure(bg="#D5BA33")
root.attributes('-fullscreen', True)
root.bind("<Escape>", lambda e: root.attributes('-fullscreen', False))

initialize_sounds()


menu_frame = create_menu(root)


root.mainloop()
