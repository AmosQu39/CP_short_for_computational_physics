# -*- coding: utf-8 -*-

import os
import tkinter as tk


def main_button():
    os.system("python main.py")


def run_button():
    run_button = tk.Button(root, text='Run', command=main_button)
    run_button.pack()


def quit_button():
    quit_button = tk.Button(root, text='Quit', command=quit)
    quit_button.pack()


if __name__ == "__main__":
    root = tk.Tk()
    run_button()
    quit_button()
    tk.mainloop()
