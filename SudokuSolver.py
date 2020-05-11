def print_board(board):
    """
    Print the sudoku board with grid lines for each mini box
    :param board: Sudoku board to print
    """
    rowlength = None

    for row in range(len(board)):
        output_str = ""

        if row !=0 and row %3 ==0 and rowlength is not None:
            print('-' * rowlength)

        for col in range(len(board[0])):

            if col != 0 and col %3 == 0:
                output_str += "|"

            if col == (len(board[0]) - 1):
                output_str += str(board[row][col])
            else:
                output_str += str(board[row][col]) + " "

        if rowlength is None:
            rowlength = len(output_str) - output_str.count("\n")

        print(output_str)

        pass

def find_empty_cell(board):
    """
    Perform BFS then DFS search to return the next available
    empty cell
    :param board: Sudoku board
    :return: Returns a tuple of (row, col) of the coordinates of the empty cell.
    Returns None if the board is completely filled.
    """
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == 0:
                return (row, col)

    else:
        return (None, None)

def is_valid(num, row, col, board):
    """
    Checks whether the number can be inserted in the position specified by
    row and column within the board
    :param num: Number to insert
    :param row: Row to check
    :param col: Column to check
    :param board: Sudoku board
    :return: True, if the position is valid for the given number and the board
    """
    for index in range(len(board)):

        # Check each row if the number is already present
        if board[row][index] == num:
           return False

        # Check each column if the number is already present
        if board[index][col] == num:
            return False

    # Find coordinates of the mini square in which the position (row, col) lies
    box_y_min = (col // 3) * 3
    box_x_min = (row // 3) * 3

    # Check within the mini square whether the number already exists
    for x in range(0, 3):
        for y in range(0, 3):
            if board[box_x_min + x][box_y_min + y] == num:
                return False
    return True

def find_solution(board):
    """
    Finds solution for the given sudoku board
    :param board: Sudoku board to solve
    :return: Returns True if a valid solution was found.
    Returns false if no solution was found.
    """

    # Find an empty cell
    (row, col) = find_empty_cell(board)

    # If there are no empty cells,
    # the board is completely filled.
    # Success!
    if row is None:
        return True


    else:
        # Check for all possible values between 1 and 9
        for num in range(1, 10):

            # If the number can be placed at the given row and column
            # Then update the board
            if is_valid(num, row, col, board):
                board[row][col] = num

                # Try to fill the next empty slot
                if find_solution(board):
                    return True

                # Reset the current empty slot at row,col if the
                # board cannot be solved with the current number
                else:
                    board[row][col] = 0

        # The board is unsolvable if no number between 1 and 9
        # can be placed in the current empty cell
        return False





