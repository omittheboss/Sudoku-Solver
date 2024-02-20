class Board:
    def __init__(self, board):
        self.board = board

    def __str__(self):
        upper_lines = f'\n╔═══{"╤═══"*2}{"╦═══"}{"╤═══"*2}{"╦═══"}{"╤═══"*2}╗\n'
        middle_lines = f'╟───{"┼───"*2}{"╫───"}{"┼───"*2}{"╫───"}{"┼───"*2}╢\n'
        lower_lines = f'╚═══{"╧═══"*2}{"╩═══"}{"╧═══"*2}{"╩═══"}{"╧═══"*2}╝\n'
        board_string = upper_lines
        for index, line in enumerate(self.board):
            row_list = []
            for square_no, part in enumerate([line[:3], line[3:6], line[6:]], start=1):
                row_square = '|'.join(str(item) for item in part)
                row_list.extend(row_square)
                if square_no != 3:
                    row_list.append('║')

            row = f'║ {" ".join(row_list)} ║\n'
            row_empty = row.replace('0', ' ')
            board_string += row_empty

            if index < 8:
                if index % 3 == 2:
                    board_string += f'╠═══{"╪═══"*2}{"╬═══"}{"╪═══"*2}{"╬═══"}{"╪═══"*2}╣\n'
                else:
                    board_string += middle_lines
            else:
                board_string += lower_lines

        return board_string

    def find_empty_cell(self):
        for row, contents in enumerate(self.board):
            try:
                col = contents.index(0)
                return row, col
            except ValueError:
                pass
        return None

    def valid_in_row(self, row, num):
        return num not in self.board[row]

    def valid_in_col(self, col, num):
        return all(
            self.board[row][col] != num
            for row in range(9)
        )

    def valid_in_square(self, row, col, num):
        row_start = (row // 3) * 3
        col_start=(col // 3) * 3
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                if self.board[row_no][col_no] == num:
                    return False
        return True

    def is_valid(self, empty, num):
        row, col = empty
        valid_in_row = self.valid_in_row(row, num)
        valid_in_col = self.valid_in_col(col, num)
        valid_in_square = self.valid_in_square(row, col, num)
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        if (next_empty := self.find_empty_cell()) is None:
            return True
        else:
            for guess in range(1, 10):
                if self.is_valid(next_empty, guess):
                    row, col = next_empty
                    self.board[row][col] = guess
                    if self.solver():
                        return True
                    self.board[row][col] = 0

        return False

def solve_sudoku(board):
    gameboard = Board(board)
    print(f'\nPuzzle to solve:\n{gameboard}')
    if gameboard.solver():
        print('\nSolved puzzle:')
        print(gameboard)

    else:
        print('\nThe provided puzzle is unsolvable.')
    return gameboard
def get_user_input():
    """Gets user input for a Sudoku board, ensuring correct format and values.

    Returns:
        A list of lists representing the Sudoku board,
        or None if invalid input is encountered.
    """

    board = []
    for _ in range(9):
        while True:
            row_str = input("Enter a row of the Sudoku board (use 0 for empty cells): ")
            row = row_str.split()

            # Validate row length
            if len(row) != 9:
                print("Invalid row length. Please enter a row with exactly 9 numbers or spaces.")
                continue

            # Validate characters and convert to integers
            try:
                row = [int(num) for num in row]
                for num in row:
                    if not 0 <= num <= 9:
                        raise ValueError("Invalid number. All numbers must be between 0 and 9.")
            except ValueError:
                print("Invalid input. Please enter only digits between 0 and 9, separated by spaces.")
                continue

            # Input is valid, break out of the loop
            break

        board.append(row)

    return board

"""puzzle = [
  [8, 9, 1, 4, 7, 3, 2, 0, 6],
  [0, 2, 0, 8, 5, 0, 3, 4, 9],
  [0, 0, 5, 9, 0, 0, 8, 0, 0],
  [0, 0, 3, 5, 0, 0, 0, 0, 7],
  [6, 0, 0, 3, 4, 0, 9, 1, 5],
  [0, 0, 0, 0, 9, 0, 0, 0, 3],
  [5, 0, 8, 0, 1, 0, 0, 6, 4],
  [0, 0, 2, 0, 0, 0, 5, 0, 0],
  [0, 7, 9, 0, 0, 5, 0, 3, 0]
]
solve_sudoku(puzzle)"""

def main():
    user_board = get_user_input()

    if user_board is not None:
        # Solve the board using solve_sudoku
        solve_sudoku(user_board)
    else:
        print("Error: Invalid input received. Please try again.")

if __name__ == "__main__":
    main()