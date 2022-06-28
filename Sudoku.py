import random

# this class contains all methods relevant to sudoku boards
class Sudoku:

    valid_group = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

    # check whether a given board is valid or not, return boolean
    @classmethod
    def check_board(cls, board):
        # check dimensions of board
        if len(board) != 9:
            return False
        for row in board:
            if len(row) != 9:
                return False

        # check actual contents of board
        return cls.check_rows(board) and cls.check_cols(board) and cls.check_grids(board)

    # check each row in the board
    @classmethod
    def check_rows(cls, board):
        for i in range(0, 9):
            # create set of integers from 1-9
            valid_check = set(cls.valid_group)

            for j in range(0, 9):
                # if exception is thrown, row contains a repeating value
                try:
                    valid_check.remove(board[i][j])
                except KeyError:
                    return False

            # if set is not empty, row does not have every integer from 1-9
            if valid_check:
                return False

        return True

    # check each column in the board
    @classmethod
    def check_cols(cls, board):
        for j in range(0, 9):
            # create set of integers from 1-9
            valid_check = set(cls.valid_group)

            for i in range(0, 9):
                # if exception is thrown, column contains a repeating value
                try:
                    valid_check.remove(board[i][j])
                except KeyError:
                    return False

            # if set is not empty, column does not have every integer from 1-9
            if valid_check:
                return False

        return True

    # check each 3x3 grid in the board
    @classmethod
    def check_grids(cls, board):
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                # if any of the grids are not valid, return false
                if not cls.check_grid(board, i, j):
                    return False

        return True

    # check a single 3x3 grid
    @classmethod
    def check_grid(cls, board, row, col):
        valid_check = set(cls.valid_group)

        for i in range(row, row+3):
            for j in range(col, col+3):
                # if exception is thrown, grid contains a repeating value
                try:
                    valid_check.remove(board[i][j])
                except KeyError:
                    return False

        # if set is not empty, grid does not have every integer from 1-9
        if valid_check:
            return False

        return True

    # generate a valid sudoku board with unique solution
    @classmethod
    def generate_board(cls):
        # start with basic valid board
        base = [
            [1, 2, 3, 4, 5, 6, 7, 8, 9],
            [4, 5, 6, 7, 8, 9, 1, 2, 3],
            [7, 8, 9, 1, 2, 3, 4, 5, 6],
            [2, 3, 4, 5, 6, 7, 8, 9, 1],
            [5, 6, 7, 8, 9, 1, 2, 3, 4],
            [8, 9, 1, 2, 3, 4, 5, 6, 7],
            [3, 4, 5, 6, 7, 8, 9, 1, 2],
            [6, 7, 8, 9, 1, 2, 3, 4, 5],
            [9, 1, 2, 3, 4, 5, 6, 7, 8]
        ]

        # call helper
        cls.generate_board_helper(base)

        return base

    @classmethod
    def generate_board_helper(cls, board):
        # randomize through number translations
        for _ in range(25):
            x = y = random.randint(1, 9)

            # make sure y is different value than x
            while y == x:
                y = random.randint(1, 9)

            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == x:
                        board[i][j] = y
                        # need to continue here to avoid overwriting in next if statement
                        continue
                    if board[i][j] == y:
                        board[i][j] = x

        return

    @classmethod
    def print_board(cls, board):
        for row in board:
            print(*row)