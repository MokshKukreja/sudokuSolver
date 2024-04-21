from tkinter import *

root = Tk()
root.geometry('330x370')
root.title("Sudoku Solver")

# Sudoku solver class
class SudokuSolver():
    def __init__(self, board):
        self.board = board
        self.setZero()
        self.solve()

    def setZero(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j].get() not in ['1','2','3','4','5','6','7','8','9']:
                    self.board[i][j].set(0)

    def solve(self):
        findEmpty = self.emptyCell()
        if not findEmpty:
            return True
        else:
            row, column = findEmpty
            for i in range(1, 10):
                if self.isValid(i, (row, column)):
                    self.board[row][column].set(i)
                    if self.solve():
                         return True
                    self.board[row][column].set(0)
            return False

    def isValid(self, num, pos):
        for i in range(9):
            if self.board[pos[0]][i].get() == str(num):
                return False

        for i in range(9):
            if self.board[i][pos[1]].get() == str(num):
                return False

        row = pos[0] // 3
        column = pos[1] // 3
        for i in range(row * 3, (row * 3) + 3):
            for j in range(column * 3, (column * 3) + 3):
                if self.board[i][j].get() == str(num):
                    return False
        return True

    def emptyCell(self):
        for row in range(9):
            for column in range(9):
                if self.board[row][column].get() == '0':
                    return (row, column)
        return None

class Interface():
    def __init__(self, window, board):
        self.window = window
        self.board = board
        self.createBoard()

    def createBoard(self):
        for row in range(9):
            for col in range(9):
                if (row < 3 or row > 5) and (col < 3 or col > 5):
                    color = 'white'
                elif (row >= 3 and row < 6) and (col >= 3 and col < 6):
                    color = 'white'
                else:
                    color = 'grey'

                self.board[row][col] = Entry(self.window, width=2, font=('Arial', 20),
                                             bg=color, cursor='arrow', borderwidth=2,
                                             highlightcolor='yellow', highlightthickness=0,
                                             highlightbackground='black', 
                                             textvariable=self.board[row][col])
                self.board[row][col].bind('<FocusIn>', self.gridChecker)
                self.board[row][col].bind('<Motion>', self.gridChecker)
                self.board[row][col].grid(row=row, column=col)

        solve = Button(self.window, text='Solve', command=self.solveSudoku)
        solve.grid(column=3, row=20)
        clear = Button(self.window, text='Clear', command=self.clearBoard)
        clear.grid(column=5, row=20)

    def gridChecker(self, event):
        for row in range(9):
            for col in range(9):
                if self.board[row][col].get() not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                    self.board[row][col].set('')

    def solveSudoku(self):
        SudokuSolver(self.board)

    def clearBoard(self):
        for row in range(9):
            for col in range(9):
                self.board[row][col].set('')

# Global 2D list which saves the values the user enters on the GUI
filledBoard = []
for row in range(9):
    filledBoard += [["", "", "", "", "", "", "", "", ""]]

for row in range(9):
    for col in range(9):
        filledBoard[row][col] = StringVar(root)

# Main Loop
Interface(root, filledBoard)
root.mainloop()
