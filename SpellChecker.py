from tkinter import *
import tkinter as tk
window = tk.Tk()

from textblob import TextBlob


def clearAll():
    word1_field.delete(0, END)
    word2_field.delete(0, END)
def correction():
    input_word = word1_field.get()
    word = TextBlob(input_word)
    corrected_word = str(word.correct())
    word2_field.insert(10, corrected_word)

if __name__ == "main":
    window = Tk()
    window.configure(background='gray')
    window.geometry("1000x450")
    window.title("Spell Corrector")
header = Label(window,
                   text='Word Correction',
                   font=('Trebuchet MS', 24, 'bold'),
                   relief=RAISED,
                   height=1,
                   bd=10,
                   padx=20,
                   pady=20,
                   width=30,
                   fg='#00FF00',
                   bg="black")


