import random
from tkinter import *
from tkinter import messagebox
from functools import partial
from itertools import chain
import random
from SudokuSetSet import SudokuSetSet

class PlaySudoku:
    def __init__(self):
        self.table = [[0 for i in range(9)] for j in range(9)]
        setSudoku = SudokuSetSet(self.table)
        self.userTable = [[0 for i in range(9)] for j in range(9)]
        self.root = Tk()
        self.root.title("SUDOKU GAME")
        self.btn_cells = [[None] * 9] * 9
        self.shownNum = -1
        self.randNums = [ ]
        self.randNumsD = { }
        self.disNums = [ ]
        self.cells = { }
        self.savePosition = (-1, -1)
        self.done = False
        self.welcome = Label(self.root, text="Welcome to Sudoku", font=('Aerial 17 bold italic'))
        self.easy = Button(self.root, text='EASY', width=25, font=('Aerial 15 bold italic'), command=lambda: self.setDifficult(1))
        self.mid = Button(self.root, text='MEDIUM', width=25, font=('Aerial 15 bold italic'), command=lambda: self.setDifficult(2))
        self.hard = Button(self.root, text='HARD', width=25, font=('Aerial 15 bold italic'), command=lambda: self.setDifficult(3))


    def setHide(self):
        numDisplay = random.randint(17, 30)

        for i in range(numDisplay):
            pos = (random.randint(0, 8), random.randint(0, 8))
            while pos in self.disNums:
                pos = (random.randint(0, 8), random.randint(0, 8))

            self.disNums.append(pos)
            self.userTable[pos[0]][pos[1]] = self.table[pos[0]][pos[1]]


    def clickNum(self, num):
        if self.checkTable():
            print("Game Done")
            self.done = True
        if not self.done:
            if self.savePosition == (-1, -1):
                return
            bname = (self.cells[self.savePosition])
            bname.configure(text=num, fg="blue", font=('Aerial 13 bold'))
            self.userTable[self.savePosition[0]][self.savePosition[1]] = num


    def clickB(self, row, column):
        self.savePosition = (row, column)

    def setDifficult(self, num):
        if num == 1:
            self.shownNum = random.randint(26, 30)
        elif num == 2:
            self.shownNum = random.randint(23, 25)
        else:
            self.shownNum = random.randint(17, 22)
        self.forgets()
        self.setHide()
        self.showTable()
    def forgets(self):
        self.welcome.pack_forget()
        self.easy.grid_forget()
        self.mid.grid_forget()
        self.hard.grid_forget()
    def callDiffButtons(self):
        self.welcome.grid()
        self.easy.grid()
        self.mid.grid()
        self.hard.grid()
    def showTable(self):
        center = Frame(self.root, bg='white', width=900, height=900, padx=3, pady=3)
        # layout all of the main containers
        self.root.grid_rowconfigure(9, weight=1)
        self.root.grid_columnconfigure(9, weight=1)
        center.grid(row=1, sticky="nsew")

        # create the center widgets
        center.grid_rowconfigure(0, weight=1)
        center.grid_columnconfigure(1, weight=1)

        blocks = []
        for i in range(3):
            row = []
            for j in range(3):
                f = Frame(center, bd=1, highlightbackground='dark blue',
                          highlightcolor='dark blue', highlightthickness=1)
                f.grid(row=i, column=j, sticky='nsew')
                row.append(f)
            blocks.append(row)
        for row in range(9):
            for column in range(9):
                frm_cell = Frame(blocks[row // 3][column // 3])
                frm_cell.grid(row=(row % 3), column=(column % 3), sticky='nsew')
                frm_cell.rowconfigure(0, minsize=50, weight=1)
                frm_cell.columnconfigure(0, minsize=50, weight=1)
                if (row, column) in self.disNums:
                    self.btn_cells[row][column] = Button(frm_cell, relief='ridge', bg='white', text=str(self.table[row][column]))
                    self.btn_cells[row][column].grid(sticky='nsew')
                    continue

                self.btn_cells[row][column] = Button(frm_cell, relief='ridge', bg='white', command=partial(self.clickB, row, column))
                self.btn_cells[row][column].grid(sticky='nsew')
                self.cells[(row, column)] = self.btn_cells[row][column]

        c = [None for i in range(9)]
        block = []
        l = Label(self.root, text="Click Button 1 - 9", font=('Aerial 17 bold italic'))
        l.grid()
        for j in range(9):
            f = Frame(center, highlightbackground='white',
                      highlightcolor='black', highlightthickness=1)
            f.grid(row=9, column=j)
            block.append(f)
        for j in range(9):
            frm_cell = Frame(block[j // 3])
            frm_cell.grid(row=10, column=(j % 3), sticky='nsew')
            frm_cell.rowconfigure(0, minsize=50, weight=1)
            frm_cell.columnconfigure(0, minsize=50, weight=1)

            c[j] = Button(frm_cell, relief='ridge', bg='black', text=j + 1, fg='dark blue',
                          font=('Aerial 17 bold italic'), command=partial(self.clickNum, j + 1))
            c[j].grid(sticky='nsew')

    def checkTable(self):
        return self.table == self.userTable


    def startGame(self):
        self.callDiffButtons()
        self.root.mainloop()
