"""
Util module to create data structure to sudoku problem
"""
def cross(rows, cols):
    """
    Method to generate a new matrix from two strings.
    Input: Rows (AB) Cols (CD)
    Output: String (AC AD  BC CD)
    """
    return [s + t for s in rows for t in cols]

def display(values):
    """
    Display the values as a 2-D grid.
    Input: The sudoku in dictionary form
    Output: None
    """
    width = 1 + max(len(values[s]) for s in BOXES)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in ROWS:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in COLS))
        if r in 'CF':
            print(line)
    return


def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Input: A grid in string form.
    Output: A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value,
            then the value will be '123456789'.
    """
    chars = []
    digits = '123456789'
    for c in grid:
        if c in digits:
            chars.append(c)
        if c == '.':
            chars.append(digits)
    assert len(chars) == 81
    return dict(zip(BOXES, chars))


ROWS = 'ABCDEFGHI'
COLS = '123456789'
BOXES = cross(ROWS, COLS)

ROWS_UNIT = [cross(r, COLS) for r in ROWS]
# Element example:
# row_units[0] = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9']
# This is the top most row.

COLUMN_UNITS = [cross(ROWS, c) for c in COLS]
# Element example:
# column_units[0] = ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1', 'I1']
# This is the left most column.

SQUARE_UNITS = [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')]
# Element example:
# square_units[0] = ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']
# This is the top left square.

UNITLIST = ROWS_UNIT + COLUMN_UNITS + SQUARE_UNITS
UNITS = dict((s, [u for u in UNITLIST if s in u]) for s in BOXES)
PEERS = dict((s, set(sum(UNITS[s], [])) - set([s])) for s in BOXES)

 # Newline at end of file
