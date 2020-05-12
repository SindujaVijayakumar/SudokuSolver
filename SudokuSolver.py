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
    Finds solution for the given sudoku board using recursion
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


def find_solution_dynamic(board):
    """
    Finds solution for the given sudoku board using a stack
    :param board: Sudoku board to solve
    :return: Returns True if a valid solution was found.
    Returns false if no solution was found.
    """

    # Initalize a stack with coordinates of empty cells
    stack = [[r, c, 0] for r in range(0, 9) for c in range(0, 9) if board[r][c] == 0]
    num_empty = len(stack)

    # Return if there are no empty cells
    if num_empty == 0:
        return True

    # Indices of row, col and intermediate value within stack items
    ROW = 0
    COL = 1
    NUM = 2

    # Status of the sudoku board
    solved = False

    # Index of the head of the stack
    stack_index  = 0
    try:
        while not solved:

            # Get the next empty cell
            row, col = stack[stack_index][ROW], stack[stack_index][COL]

            # Start testing numbers greater than the last value stored at the empty cell
            min = stack[stack_index][NUM] + 1
            for num in range(min, 10):

                # Check whether the number is valid for the current sudoku baard
                if is_valid(num, row, col, board):

                    # Update the empty cell
                    board[row][col] = num

                    # Update stack with the latest value at the empty cell
                    stack[stack_index][NUM] = num

                    # Increment stack head
                    stack_index += 1

                    if stack_index == num_empty:
                        # If all empty cells have been filled,
                        # Success!
                        return True

                    # Go back to while loop to solve the board
                    break
            else:
                # All numbers from 1 to 9 are invalid for the current empty cell

                # Reset current empty cell
                board[row][col] = 0

                # Reset the latest value stored in the stack
                stack[stack_index][NUM] = 0

                # Decrement stack head
                stack_index -= 1

                if stack_index < 0:
                    # No combination of numbers could solve the board
                    # FAIL
                    return False
                pass
            pass

    except Exception as ex:

        print("stack_index = {}, stack_size = {}". format(stack_index, len(stack)))
        #print_board(board)
        raise ex



    pass


