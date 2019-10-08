############################################################
# CIS 521: Homework 4
############################################################

student_name = "Jerrison Li"

############################################################
# Imports
############################################################

# Include your imports here, if any are used.
import pathlib
import copy
import random

############################################################
# Section 1: Sudoku Solver
############################################################


def sudoku_cells():
    return [(row, col) for row in range(9) for col in range(9)]


def sudoku_arcs():
    arcs = set()
    # same 9 box
    for i in range(9):
        for j in range(9):
            for k in range(3):
                for l in range(3):
                    x = int(i / 3) * 3 + k
                    y = int(j / 3) * 3 + l
                    if i != x or j != y:
                        arcs.add(((i, j), (x, y)))
    # row, col, and diagonal
    for i in range(9):
        for j in range(9):
            for k in range(9):
                if k != j:
                    arcs.add(((i, j), (i, k)))
                    arcs.add(((j, i), (k, i)))
    return arcs


def read_board(path):
    board = {}
    cell_list = []

    filepath = pathlib.Path.cwd() / path
    fh = open(filepath)

    for line in fh:
        line = line.strip()
        cell_list.append(line)
    fh.close()

    row = 0
    for i in cell_list:
        col = 0
        for element in i:
            if element == "*":
                board[(row, col)] = set([1, 2, 3, 4, 5, 6, 7, 8, 9])
            else:
                board[(row, col)] = set([int(element)])
            col += 1
        row += 1
    return board


class Sudoku(object):

    CELLS = sudoku_cells()
    ARCS = sudoku_arcs()

    def __init__(self, board):
        self.board = board
        self.confirm = 0

    def get_values(self, cell):
        return self.board.get(cell)

    def remove_inconsistent_values(self, cell1, cell2):
        target_set = self.board.get(cell2)
        if len(target_set) != 1:
            return False
        target_num_int = next(iter(target_set))
        if target_num_int in self.board.get(cell1):
            self.board.get(cell1).remove(target_num_int)
            return True
        else:
            return False

    def successors(self, cell):
        successors = set()
        for row in range(9):
            if row != cell[0]:
                successors.add((row, cell[1]))
        for col in range(9):
            if col != cell[1]:
                successors.add((cell[0], col))
        for i in range(3):
            for j in range(3):
                x = int(cell[0] / 3) * 3 + i
                y = int(cell[1] / 3) * 3 + j
                if x != cell[0] or y != cell[1]:
                    successors.add((x, y))
        return successors

    def infer_ac3(self):
        queue = []
        for arc in self.ARCS:
            queue.append(arc)
        while queue:
            arc = queue.pop()
            if len(self.board[arc[0]]) > 1 and len(self.board[arc[1]]) == 1:
                if self.remove_inconsistent_values(arc[0], arc[1]):
                    for successor in self.successors(arc[0]):
                        queue.append((successor, arc[0]))

    def is_in_block(self, value, element):
        block_row_start = int(element[0] / 3) * 3
        block_col_start = int(element[1] / 3) * 3
        for i in range(block_row_start, block_row_start + 3):
            for j in range(block_col_start, block_col_start + 3):
                if i != element[0] or j != element[1]:
                    if value in self.board[(i, j)]:
                        return True
        return False

    def is_in_row(self, value, element):
        for j in range(0, 9):
            if j != element[1]:
                if value in self.board[(element[0], j)]:
                    return True
        return False

    def is_in_col(self, value, element):
        for i in range(0, 9):
            if i != element[0]:
                if value in self.board[(i, element[1])]:
                    return True
        return False

    def is_solved(self):
        for cell in self.CELLS:
            if len(self.board.get(cell)) != 1:
                return False
        return True

    def infer_improved(self):
        while 1:
            self.infer_ac3()
            if self.is_solved():
                return self
            for i in range(0, 9):
                for j in range(0, 9):
                    element = (i, j)
                    if len(self.board[element]) > 1:
                        for value in self.board[element]:
                            if not self.is_in_col(value, element):
                                self.board[element] = set([value])
                            if not self.is_in_block(value, element):
                                self.board[element] = set([value])
                            if not self.is_in_row(value, element):
                                self.board[element] = set([value])
        return self

    def set_store(self):
        return {1: [0], 2: [0], 3: [0], 4: [0], 5: [0], 6: [0], 7: [0], 8: [0], 9: [0]}

    def com_solve(self):
        explored1 = []
        explored2 = []
        count = 0
        for i in range(9):
            for j in range(9):
                cell1 = (i, j)
                cell2 = (j, i)
                value1 = self.board[cell1]
                value2 = self.board[cell2]
                if len(value1) == 1:
                    count += 1
                    if list(value1)[0] in explored1:
                        return (False, 0)
                    else:
                        explored1.append(list(value1)[0])
                if len(value2) == 1:

                    if list(value2)[0] in explored2:
                        return (False, 0)
                    else:
                        explored2.append(list(value2)[0])
            explored1 = []
            explored2 = []
        explored3 = []
        for i in range(3):
            for j in range(3):
                for ci in range(3):
                    for cj in range(3):
                        cell3 = (i * 3 + ci, j * 3 + cj)
                        value3 = self.board[cell3]
                        if len(value3) == 1:

                            if list(value3)[0] in explored3:
                                return (False, 0)
                            else:
                                explored3.append(list(value3)[0])
                explored3 = []
        return (True, count)

    def update_cell(self, type):
        changed = False
        store = self.set_store()

        if type == "block":
            for i in range(3):
                for j in range(3):

                    for ci in range(3):
                        for cj in range(3):
                            cell = (i * 3 + ci, j * 3 + cj)
                            if len(self.board[cell]) == 1:
                                continue
                            else:
                                key = self.board[cell]
                                for every_key in key:
                                    store[every_key][0] += 1
                                    store[every_key].append(cell)
                    for _key in store.keys():
                        if store[_key][0] == 1:
                            changed = True
                            rst = set()
                            rst.add(_key)
                            c_cell = store[_key][1]
                            self.board.update({c_cell: rst})
                            if len(rst) == 1:
                                self.confirm += 1
                            break
                    store = self.set_store()
            return changed

        if type == "row":
            for i in range(9):
                for j in range(9):
                    cell = (i, j)
                    if len(self.board[cell]) == 1:
                        continue
                    else:
                        key = self.board[cell]
                        for every_key in key:
                            store[every_key][0] += 1
                            store[every_key].append(cell)
                for _key in store.keys():
                    if store[_key][0] == 1:
                        changed = True
                        rst_r = set()
                        rst_r.add(_key)
                        c_cell = store[_key][1]
                        self.board.update({c_cell: rst_r})
                        if len(rst_r) == 1:
                            self.confirm += 1
                        break
                store = self.set_store()
        return changed

        if type == "column":
            for i in range(9):
                for j in range(9):
                    cell = (j, i)
                    if len(self.board[cell]) == 1:
                        continue
                    else:
                        key = self.board[cell]
                        for every_key in key:
                            store[every_key][0] += 1
                            store[every_key].append(cell)
                for _key in store.keys():
                    if store[_key][0] == 1:
                        changed = True
                        rst = set()
                        rst.add(_key)
                        cell = store[_key][1]
                        self.board.update({cell: rst})
                        if len(rst) == 1:
                            self.confirm += 1
                        break
                store = self.set_store()
        return changed

    def shuffle(self):
        improve_finish = True
        self.infer_ac3()
        while improve_finish:
            a = 0
            if self.update_cell("block"):
                self.infer_ac3()
                a += 1
            if self.update_cell("row"):
                self.infer_ac3()
                a += 1
            if self.update_cell("column"):
                self.infer_ac3()
                a += 1
            if a == 0:
                improve_finish = False

    def helper(self, que):

        self.shuffle()
        s = self.com_solve()
        if s == (True, 81):
            return self

        if not s[0]:
            return False

        for i in range(9):
            for j in range(9):
                cell = (i, j)

                if len(self.board[cell]) > 1:
                    f2 = set()
                    fi_set = set()
                    cc = 0
                    for _ii in self.board[cell]:
                        if not cc:
                            fi_set.add(_ii)
                        else:
                            f2.add(_ii)
                        cc += 1

                    future_board = {i2: self.board[i2] for i2 in self.board}
                    future_board.update({cell: f2})

                    self.board.update({cell: fi_set})

                    que.append(future_board)
                    result = self.helper(que)

                    if result:
                        return True

                    while not result:
                        self.board = que.pop()
                        result = self.helper(que)
                        if result:
                            return True

    def infer_with_guessing(self):
        queue = []

        self.helper(queue)
        return 1


############################################################
# Section 2: Dominoes Games
############################################################


def create_dominoes_game(rows, cols):
    return DominoesGame([[False for i in range(cols)] for j in range(rows)])


class DominoesGame(object):

    # Required
    def __init__(self, board):
        self.board = board
        self.rows = len(board)
        self.columns = len(board[0])

    def get_board(self):
        return self.board

    def reset(self):
        self.board = [[False for i in range(self.columns)] for j in range(self.rows)]

    def is_legal_move(self, row, col, vertical):
        if row < 0 or row >= self.rows or col < 0 or col >= self.columns:
            return False
        if vertical:
            if row + 1 >= self.rows:
                return False
            if self.board[row][col] or self.board[row + 1][col]:
                return False
            else:
                return True
        else:
            if col + 1 >= self.columns:
                return False
            if self.board[row][col] or self.board[row][col + 1]:
                return False
            else:
                return True

    def legal_moves(self, vertical):
        for y in range(self.rows):
            for x in range(self.columns):
                if self.is_legal_move(y, x, vertical):
                    yield (y, x)

    def perform_move(self, row, col, vertical):
        if self.is_legal_move(row, col, vertical):
            if vertical:
                self.board[row][col] = True
                self.board[row + 1][col] = True
            else:
                self.board[row][col] = True
                self.board[row][col + 1] = True

    def game_over(self, vertical):
        if len(list(self.legal_moves(vertical))) > 0:
            return False
        else:
            return True

    def copy(self):
        return copy.deepcopy(self)

    def successors(self, vertical):
        for y, x in self.legal_moves(vertical):
            new_game = self.copy()
            new_game.perform_move(y, x, vertical)
            yield ((y, x), new_game)

    def get_random_move(self, vertical):
        y, x = random.choice(list(self.legal_moves(vertical)))
        self.perform_move(y, x, vertical)

    # Required
    def get_best_move(self, vertical, limit):

        a = float("-inf")
        b = float("inf")

        def utility(state):
            return len(list(state.legal_moves(True))) - len(
                list(state.legal_moves(False))
            )

        def alphabeta(state, alpha, beta, depth, v):
            best_move = None
            if depth == 0 or state.game_over(v):
                alphabeta.num_nodes += 1
                return None, utility(state), alphabeta.num_nodes
            if v:
                for (y, x), new_game in state.successors(v):
                    old_alpha = alpha
                    # print (y, x, v)
                    alpha = max(
                        alpha, alphabeta(new_game, alpha, beta, depth - 1, not v)[1]
                    )
                    if alpha != old_alpha:
                        best_move = (y, x)
                    if alpha >= beta:
                        break
                return best_move, alpha, alphabeta.num_nodes
            else:
                for (y, x), new_game in state.successors(v):
                    old_beta = beta
                    beta = min(
                        beta, alphabeta(new_game, alpha, beta, depth - 1, not v)[1]
                    )
                    if beta != old_beta:
                        best_move = (y, x)
                    if alpha >= beta:
                        break
                return best_move, beta, alphabeta.num_nodes

        alphabeta.num_nodes = 0

        best_next_move, value, number = alphabeta(self, a, b, limit, vertical)
        if vertical:
            return best_next_move, value, number
        else:
            return best_next_move, -value, number


############################################################
# Section 3: Feedback
############################################################

# Just an approximation is fine.
feedback_question_1 = 20

feedback_question_2 = """
Figuring how to generate the successors for each cell
"""

feedback_question_3 = """
I liked the fact that I learned different sudoku strategies while doing the
homework.
"""
