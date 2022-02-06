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
    licensewin = tk.Tk()
    # Add a title
    licensewin.title("License")

    # Set the GUI Size
    licensewin.geometry("640x360")

    # Disable resizing the GUI by passing in False/False
    licensewin.resizable(False, False)

    licenselable = tk.Label(licensewin, text="""
    MIT License
    
    Copyright (c) 2022 MinseoKang
    
    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:
    
    The above copyright notice and this permission notice shall be included in all
    copies or substantial portions of the Software.
    
    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
    SOFTWARE.
    """)
    licenselable.pack()

    # mainloop
    licensewin.mainloop()


# ==================
# main function
# ==================


def menu_gui(instance):

    # Making menu instance
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
