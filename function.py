from utils import *

def grid_values(grid):
    """Convert grid string into {<box>: <value>} dict with '.' value for empties.

    Args:
        grid: Sudoku grid in string form, 81 characters long
    Returns:
        Sudoku grid in dictionary form:
        - keys: Box labels, e.g. 'A1'
        - values: Value in corresponding box, e.g. '8', or '.' if it is empty.
    """
    assert len(grid) == 81, "Input grid must be a string of length 81 (9x9)"
    return dict(zip(BOXES, grid))

def grid_values2(grid):
    values={}
    for v in range(len(grid)):
        values.update({BOXES[v]:grid[v]})
    return values

def grid_possibilites(grid):
    dic={}
    all_values = '123456789'

    for v in range(len(grid)):
        if(grid[v] == '.'):
            dic.update({BOXES[v]:all_values})
        else:
            dic.update({BOXES[v]:grid[v]})
    return dic

def grid_possibilites_udacity(grid):
    values = []
    all_digits = '123456789'
    for c in grid:
        if c == '.':
            values.append(all_digits)
        elif c in all_digits:
            values.append(c)
    assert len(values) == 81
    return dict(zip(BOXES, values))
def eliminate(values):
    ws = []
    for box in values.keys():
        if(len(values[box])==1):
            ws.append(box)
    for box in ws:
        digit = values[box]
        for peer in PEERS[box]:
            values[peer] = values[peer].replace(digit,'')
    return values
def eliminate_udacity(values):
    ws = [box for box in values.keys() if len(values[box]) == 1]
    for box in ws:
        digit = values[box]
        for peer in PEERS[box]:
            values[peer] = values[peer].replace(digit, '')
    return values
def only_choice(values):
    for unit in UNITLIST:
        for digit in '123456789':
            dplaces = [box for box in unit if digit in values[box]]
            if len(dplaces) == 1:
                values[dplaces[0]] = digit
    return values
# Newline at end of file