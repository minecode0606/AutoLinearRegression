# ==================
# imports
# ==================
from re import I
import tkinter as tk  # import Tkinter
from SettingGUI.GUI_Basic_Setting import frame_GUI
from SettingGUI.GUI_menu_Setting import menu_GUI

# create instance
win = tk.Tk()

# Making the Frame
frame_GUI(win)

# Making the Menu
menu_GUI(win)

# =================
# Start GUI
# =================
win.mainloop()
