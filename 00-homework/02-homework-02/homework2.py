############################################################
# CIS 521: Homework 2
############################################################

student_name = "Jerrison Li"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math
import numpy as np
import copy
import random


############################################################
# Section 1: N-Queens
############################################################


def num_placements_all(n):
    """Returns number of ways you can place n queens in an n*n board"""
    return math.factorial(n ** 2) / (math.factorial(n ** 2 - n) * math.factorial(n))


def num_placements_one_per_row(n):
    """Returns number of ways you can place n queens in an n*n board but with 
    none of them in the same row"""
    return n ** n


def n_queens_valid(board):
    """Checks if a particular placement of a number of queens is valid. First
    checks if there are any queens in the same column, then checks that no
    queens are in the same diagonal.
    
    Return True if valid, False otherwise"""

    # Check that no columns are repeated
    if (len(board) == 0) or (len(board) == 1):
        return True

    if len(board) > len(set(board)):
        return False

    for i in range(len(board)):
        # check rows below
        for j in range(1, len(board) - i):
            if board[i] + j == board[i + j]:
                return False
        # check rows above
        for j in range(1, len(board) - i):
            if board[i] - j == board[i + j]:
                return False

    return True


def n_queens_solutions(n):
    """Yield all valid placements of n queens on an n x n board"""

    border = [[]]  # initialize empty state

    while 1:
        if not border:
            return
        child = border.pop()

        for i in range(n):
            board = child + [i]
            if n_queens_valid(board):
                if len(board) == n:
                    yield board
                else:
                    border.append(board)


############################################################
# Section 2: Lights Out
############################################################


class LightsOutPuzzle(object):
    def __init__(self, board):
        self.board = board

    def get_board(self):
        return self.board

    def perform_move(self, row, col):
        # itself
        self.board[row][col] = not self.board[row][col]

        # up
        if row != 0:
            self.board[row - 1][col] = not self.board[row - 1][col]

        # down
        if row != len(self.board) - 1:
            self.board[row + 1][col] = not self.board[row + 1][col]

        # left
        if col != 0:
            self.board[row][col - 1] = not self.board[row][col - 1]

        # right
        if col != len(self.board[0]) - 1:
            self.board[row][col + 1] = not self.board[row][col + 1]
        # pass

    def scramble(self):
        for i in range(0, len(self.board)):
            for j in range(0, len(self.board[0])):
                if random.random() < 0.5:
                    self.perform_move(i, j)

    def is_solved(self):
        for i in range(len(self.get_board())):
            for j in range(len(self.get_board()[0])):
                if self.board[i][j]:
                    return False

        return True

    def copy(self):
        return copy.deepcopy(self)

    def successors(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                temp = self.copy()
                temp.perform_move(i, j)
                yield ((i, j), temp)

    def find_solution(self):
        # return [(0, 0), (0, 2)]
        pass


def create_puzzle(rows, cols):
    return LightsOutPuzzle(np.zeros((rows, cols), dtype=bool).tolist())


############################################################
# Section 3: Linear Disk Movement
############################################################


def solve_identical_disks(length, n):
    pass


def solve_distinct_disks(length, n):
    pass


############################################################
# Section 4: Feedback
############################################################

feedback_question_1 = """
20 hours
"""

feedback_question_2 = """
Implementation of algorithms.
"""

feedback_question_3 = """
I would have changed the treatment of the problems.
"""
