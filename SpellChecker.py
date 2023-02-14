from tkinter import *
import tkinter as tk
window = tk.Tk()

from textblob import TextBlob


def clearAll():
    word1_field.delete(0, END)
    word2_field.delete(0, END)


