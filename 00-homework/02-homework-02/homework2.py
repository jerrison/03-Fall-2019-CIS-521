############################################################
# CIS 521: Homework 2
############################################################

student_name = "Jerrison Li"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import math

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
    for i in range(len(n)):
        pass


def n_queens_helper(n, board):
    """Helper function
    Why does the homework specify that I need an n for it?
    I think it's because I supply a whole board but then use n so that the
    function knows what portion of the board to evaluate."""

    if n_queens_valid(board) == True:
        return board


############################################################
# Section 2: Lights Out
############################################################


class LightsOutPuzzle(object):
    def __init__(self, board):
        pass

    def get_board(self):
        pass

    def perform_move(self, row, col):
        pass

    def scramble(self):
        pass

    def is_solved(self):
        pass

    def copy(self):
        pass

    def successors(self):
        pass

    def find_solution(self):
        pass


def create_puzzle(rows, cols):
    pass


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
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_2 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""

feedback_question_3 = """
Type your response here.
Your response may span multiple lines.
Do not include these instructions in your response.
"""
