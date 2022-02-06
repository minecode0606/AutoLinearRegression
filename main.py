# ==================
# imports
# ==================
# import Tkinter
import tkinter as tk
# import functions
from SettingGUI.GUI_Basic_Setting import basic_frame_gui, frame_GUI
from SettingGUI.GUI_menu_Setting import menu_gui

# =================
# Making GUI
# =================
# create instance
win = tk.Tk()

# Making the Frame
basic_frame_gui(win)

# Making the Menu
menu_gui(win)

frame_GUI(win)
# =================
# Start GUI
# =================
win.mainloop()
