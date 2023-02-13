from tkinter import *
from textblob import TextBlob

def clearAll():
    word1_field.delete(0, END)
    word2_field.delete(0, END)

def correction():
    input_word = word1_field.get()
    word = TextBlob(input_word)
    corrected_word = str(word.correct())
    word2_field.insert(10, corrected_word)


