############################################################
# CIS 521: Homework 3
############################################################

student_name = "Jerrison Li"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import itertools
import copy
import random
import queue

############################################################
# Section 1: Tile Puzzle
############################################################


def create_tile_puzzle(rows, cols):
    empty_list = []
    element_list = itertools.cycle(range(rows * cols))
    next(element_list)  # start at 1 and cycle back to 0

    for i in range(rows):
        new_list = []
        for j in range(cols):
            new_list.append(next(element_list))
        empty_list.append(new_list)

    return TilePuzzle(empty_list)


class TilePuzzle(object):

    # Required
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.cols = len(board[0])

        # Find where 0
        for i in range(len(self.board)):
            try:
                j = self.board[i].index(0)
            except ValueError:
                pass
            else:
                self.zero_row = i
                self.zero_col = j

    def get_board(self):
        return self.board

    def perform_move(self, direction):

        if direction.lower() == "up":
            # Up
            if self.zero_row == 0:
                return False
            else:
                self.board[self.zero_row][self.zero_col] = self.board[
                    self.zero_row - 1
                ][self.zero_col]
                self.board[self.zero_row - 1][self.zero_col] = 0
                self.zero_row = self.zero_row - 1
                return True
        elif direction.lower() == "down":
            # Down
            if self.zero_row == len(self.board) - 1:
                return False
            else:
                self.board[self.zero_row][self.zero_col] = self.board[
                    self.zero_row + 1
                ][self.zero_col]
                self.board[self.zero_row + 1][self.zero_col] = 0
                self.zero_row = self.zero_row + 1
                return True
        elif direction.lower() == "left":
            # Left
            if self.zero_col == 0:
                return False
            else:
                self.board[self.zero_row][self.zero_col] = self.board[self.zero_row][
                    self.zero_col - 1
                ]
                self.board[self.zero_row][self.zero_col - 1] = 0
                self.zero_col = self.zero_col - 1
                return True
        elif direction.lower() == "right":
            # Left
            if self.zero_col == len(self.board[0]) - 1:
                return False
            else:
                self.board[self.zero_row][self.zero_col] = self.board[self.zero_row][
                    self.zero_col + 1
                ]
                self.board[self.zero_row][self.zero_col + 1] = 0
                self.zero_col = self.zero_col + 1
                return True
        else:
            return False

    def scramble(self, num_moves):
        for i in range(num_moves):
            self.perform_move(random.choice(["up", "down", "left", "right"]))

    def is_solved(self):
        return self.board == create_tile_puzzle(self.rows, self.cols).get_board()

    def copy(self):
        return copy.deepcopy(self)

    def successors(self):
        moves = ["up", "down", "left", "right"]
        for move in moves:
            new_p = self.copy()
            if new_p.perform_move(move):
                yield (move, new_p)

    # Required
    def find_solutions_iddfs(self):
        "Iterative deepening depth-first search (IDDFS)"
        limit = 1
        solved = False
        while not solved:
            for solution in self.iddfs_helper(limit, []):
                if solution:
                    yield solution
                    solved = True
            limit += 1

    def iddfs_helper(self, limit, moves):
        """Helper recursion function for find_solutions_iddfs"""
        if limit == 0:
            if self.is_solved():
                yield moves
            else:
                yield False
        else:
            for move, new_p in self.successors():
                for solution in new_p.iddfs_helper(limit - 1, moves + [move]):
                    yield solution

    # Required
    def find_solution_a_star(self):
        """Find optimal solution"""
        frontier = queue.PriorityQueue()
        frontier.put((self.manhattan_distance(), self))
        g_n = {self: 0}

        explored = set()

        solution = []
        current_distance = 0

        while not frontier.empty():
            current = frontier.get()

            if current.is_solved():
                return solution

            explored.add(current.get_board())

            for move, successor in current.get_successors():
                # need distance from start position (maybe use manhattan distance but not from solved)?
                new_distance = g_n[current] + 1 + successor.manhattan_distance()
                if (
                    successor.get_board() not in explored
                    or successor.get_board() not in frontier
                ):
                    pass

        # while True:
        #     for move, successor in self.successors():
        #         if successor.get_board() not in closed_list:
        #             closed_list.append(successor.get_board())
        #             print(
        #                 move,
        #                 successor.get_board(),
        #                 successor.manhattan_distance(),
        #                 self.get_board(),
        #                 self.manhattan_distance(),
        #                 solution,
        #                 visited,
        #             )
        #             if successor.manhattan_distance() < self.manhattan_distance():
        #                 solution.append(move)
        #                 self.perform_move(move)
        #                 current_distance = self.manhattan_distance()
        #
        # return solution

    def manhattan_distance(self):
        """Calculates Manhattan distance heuristic"""

        manhattan_distance = 0

        solved_board = create_tile_puzzle(self.rows, self.cols)

        for row in range(self.rows):
            for col in range(self.cols):

                # Find value in each place
                val = self.board[row][col]
                if val == 0:
                    continue
                # print(row, col, val)

                # Find where it should be
                correct_location = [
                    (index, row.index(val))
                    for index, row in enumerate(solved_board.get_board())
                    if val in row
                ]

                correct_row = correct_location[0][0]
                correct_col = correct_location[0][1]

                # print("desired row and column = ", (correct_row, correct_col))
                manhattan_distance += abs(correct_row - row) + abs(correct_col - col)

        return manhattan_distance


############################################################
# Section 2: Grid Navigation
############################################################


def find_path(start, goal, scene):
    pass


############################################################
# Section 3: Linear Disk Movement, Revisited
############################################################


def solve_distinct_disks(length, n):
    pass


############################################################
# Section 4: Feedback
############################################################

# Just an approximation is fine.
feedback_question_1 = 0

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


# p = create_tile_puzzle(3, 3)
# for move, new_p in p.successors():
#     print(move, new_p.get_board())

# p = create_tile_puzzle(3, 3)
# p.perform_move("up")
# print(p.manhattan_distance())

# b = [[4, 1, 2], [0, 5, 3], [7, 8, 6]]
# p = TilePuzzle(b)
# p.find_solution_a_star()

b = [[1, 2, 3], [4, 0, 5], [6, 7, 8]]
p = TilePuzzle(b)
for move, new_p in p.successors():
    print(move, new_p.get_board())

# b = [[4, 1, 2], [0, 5, 3], [7, 8, 6]]
# p = TilePuzzle(b)
# p.perform_move("left")
# print(p.manhattan_distance())
#
#
# p = create_tile_puzzle(3, 3)
# print(p.manhattan_distance())
