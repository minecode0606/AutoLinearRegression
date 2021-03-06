"""
이 파일은 GUI개발을 위해 기본설정을 하는 함수를 다룹니다.
"""
# ==================
# imports
# ==================

import tkinter as tk

# ==================
# function
# ==================
def basic_frame_gui(instance):
    """
    이 함수는 GUI를 구성하는 화면의 틀을 설정합니다.
    :param instance:
    :return:
    """
    # Add a title
    instance.title("AutoRegression")

    # Set the GUI Size
    instance.geometry("768x480")
    # Disable resizing the GUI by passing in False/False
    instance.resizable(False, False)


def frame_GUI(instance):
    add_file_button = tk.Button(instance, text="파일추가")
    add_file_button.grid(row=0, column=0)
    add_file_button.pack()
