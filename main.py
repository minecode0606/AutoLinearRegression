# ==================
# imports
# ==================
import tkinter as tk  # import Tkinter
from SettingGUI.GUI_Basic_Setting import frame_gui
from SettingGUI.GUI_menu_Setting import menu_gui

# create instance
win = tk.Tk()

# Making the Frame
frame_gui(win)

# Making the Menu
menu_gui(win)

# =================
# Start GUI
# =================
win.mainloop()
