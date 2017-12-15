from util_udacity import *
import operator
def search(values):
    "Using depth-first search and propagation, create a search tree and solve the sudoku."
    # First, reduce the puzzle using the previous function
    values = reduce_puzzle(values)

    # Choose one of the unfilled squares with the fewest possibilities
    options = sorted(values.items(), key=operator.itemgetter(1))

    # Now use recursion to solve each one of the resulting sudokus, and if one returns a value (not False), return that answer!

    # If you're stuck, see the solution.py tab!

def solve(values):
    "Recursion Method"
    if all(len(values[s]) == 1 for s in boxes): 
        return True
    else:
        pass
