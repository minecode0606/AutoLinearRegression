# ==================
# imports
# ==================

import tkinter as tk

# ==================
# sub function
# ==================


def show_intro():
    pass


def show_license():
    pass

# ==================
# main function
# ==================


def menu_gui(instance):

    menu = tk.Menu(instance)

    # Making File_Menu
    menu_file = tk.Menu(menu, tearoff=0)
    menu_file.add_command(label="Introduction", command=show_intro)
    menu_file.add_separator()
    menu_file.add_command(label="License", command=show_license)
    menu_file.add_separator()

    # add the menu
    menu.add_cascade(label="File", menu=menu_file)

    # comfig menu
    instance.config(menu=menu)
