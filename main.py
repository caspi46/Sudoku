# This is a sample Python script.
from tkinter import *
from SudokuSudoku import PlaySudoku
from tkinter import messagebox
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from SudokuSudoku import PlaySudoku

def print_hi(name):
    window = Tk()
    window.title("Welcome to Sudoku")
    window.geometry('350x200')
    window.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    a = PlaySudoku()
    a.startGame()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
