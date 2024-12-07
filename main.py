from tkinter import Tk, Frame
from menu import create_menu
from utils.sounds import initialize_sounds
from utils.loggers import FileLogger, ConsoleLogger, MultiLogger


root = Tk()
root.title("Warcraft IV")
root.geometry("1000x800")
root.configure(bg="#D5BA33")
root.attributes('-fullscreen', True)
root.bind("<Escape>", lambda e: root.attributes('-fullscreen', False))

file_logger = FileLogger("game_logs.txt")
console_logger = ConsoleLogger()
logger = MultiLogger(file_logger, console_logger)
logger.log("info", "Game started.")

initialize_sounds()

menu_frame = create_menu(root)


root.mainloop()
