# SudokuSolver
Solve sudoku using Python

SudokuSolver.py solves a board by doing a Breadth First Search for an empty cell and then fills it with a value between 1 and 9 such that:
1. It is unique in a row
2. It is unique in a column
3. It is unique in a mini-square


How to test SudokuSolver.py?
1. Specify your board as a list of lists in Test/testinput.py
2. Run Test/test_SudokuSolver.py

How to generate testinput.py from https://qqwing.com/generate.html ?
1. Go to https://qqwing.com/generate.html
2. Specify output format as compact
3. Copy generated sudoku board into Test/raw_input.py
4. Run Test/testinput_generator.py
