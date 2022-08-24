import random
from tkinter import *
from tkinter import messagebox
from functools import partial
from itertools import chain
import random

class PlaySudoku:
    def __init__(self):
        self.table = [[0 for i in range(9)] for j in range(9)]
        self.root = Tk()
        self.root.title("Welcome to Sudoku")
        self.btn_cells = [[None] * 9] * 9
        self.shownNum = random.randint(17, 30)
        self.randNums = [ ]
        self.randNumsD = { }
        self.setRand()
        self.cells = { }
        self.savePosition = (-1, -1)
        self.done = False
        self.rangeList = [ ]
        self.setRangeList()

    def setRangeList(self):
        r = (-1, -1)
        l = (-1, -1)
        for i in range(3):
            if i * 2 in range(0, 3):
                r = range(0, 3)
            elif i * 2 in range(3, 6):
                r = range(3, 6)
            else:
                r = range(6, 9)
            for j in range(3):
                if i * 2 in range(0, 3):
                    l = range(0, 3)
                elif i * 2 in range(3, 6):
                    l = range(3, 6)
                else:
                    l = range(6, 9)
                self.rangeList.append((r, l))

    def setHori(self, r):
        return self.table[r]

    def setVert(self, c):
        return [self.table[i][c] for i in range(9)]

    def setSquare(self, rr, cr):
        cantS = []
        for i in rr:
            for j in cr:
                cantS.append(self.table[i][j])
        return cantS

    def setRand(self):
        for i in range(self.shownNum):
            r = random.randint(0, 8)
            c = random.randint(0, 8)

            rr = self.checkSquare(r)
            cr = self.checkSquare(c)

            while i != 0 and (r, c) in self.randNums:
                r = random.randint(0, 8)
                c = random.randint(0, 8)

            self.randNums.append((r, c))
            v = random.randint(1, 9)
            cantC = self.setHori(r)
            cantR = self.setVert(c)
            cantS = self.setSquare(rr, cr)

            while v in cantC or v in cantR or v in cantS:
                v = random.randint(1, 9)
            self.table[r][c] = v
            self.randNumsD[(r, c)] = v

    def checkSquare(self, i):
        if i in range(0, 3):
            return range(0, 3)
        elif i in range(3, 6):
            return range(3, 6)
        else:
            return range(6, 9)

    def clickNum(self, num):
        if not (0 in chain(*self.table)):
            self.checkTable()
        if self.done == False:
            if self.savePosition == (-1, -1):
                return
            bname = (self.cells[self.savePosition])
            bname.configure(text=num, fg="blue", font=('Aerial 13 bold'))


    def clickB(self, row, column):
        self.savePosition = (row, column)

    def showTable(self):
        l = Label(self.root, text="Welcome to Sudoku", font=('Aerial 17 bold italic'))
        l.pack()
        center = Frame(self.root, bg='white', width=900, height=900, padx=3, pady=3)
        # layout all of the main containers
        self.root.grid_rowconfigure(9, weight=1)
        self.root.grid_columnconfigure(9, weight=1)
        center.pack()

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
                if (row, column) in self.randNums:
                    self.btn_cells[row][column] = Button(frm_cell, relief='ridge', bg='white', text=str(self.randNumsD[(row, column)]))
                    self.btn_cells[row][column].grid(sticky='nsew')
                    continue

                self.btn_cells[row][column] = Button(frm_cell, relief='ridge', bg='white', command=partial(self.clickB, row, column))
                self.btn_cells[row][column].grid(sticky='nsew')
                self.cells[(row, column)] = self.btn_cells[row][column]

        c = [None for i in range(9)]
        block = []
        l = Label(self.root, text="Click Button 1 - 9", font=('Aerial 17 bold italic'))
        l.pack()
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
        for i in range(9):
            v = [ ]
            v.append(self.table[i][0])
            h = [ ]
            h.append(self.table[0][i])
            for j in range(9):
                if j != 0 and (self.table[i][j] in v or self.table[j][i] in h):
                    return False

            for i in self.rangeList:
                for j in i[0]:
                    v = []
                    for k in i[1]:
                        if bool(v):
                            v.append(self.table[j][k])
                            continue
                        if self.table[j][k] in v:
                            return False

            self.done = True
            return True





    def startGame(self):
        self.showTable()
        self.root.mainloop()
