from SudokuSolver import *
from Test.testinput import board
import cProfile
import time
import copy

if __name__ == "__main__":
    test_board1 = copy.deepcopy(board)
    test_board2 = copy.deepcopy(board)
    test_board3 = copy.deepcopy(board)
    test_board4 = copy.deepcopy(board)

    print_board(board)
    print("-------------------------------------------")
    print(" Solving board using recursion ")
    find_solution(test_board1)
    print_board(test_board1)
    time.sleep(2)
    print("-------------------------------------------")
    print(" Solving board using dynamic programming ")
    find_solution_dynamic(test_board2)
    print_board(test_board2)



    cProfile.run("find_solution_dynamic(test_board3)", sort = "cumtime")
    cProfile.run("find_solution(test_board4)", sort="cumtime")


