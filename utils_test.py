import unittest
from utils import *
from function import *
# 2 empty lines between top-level funcs + classes


class SudokuTest(unittest.TestCase):

    def test_cross(self):
        self.assertEqual(['ad', 'ae', 'af', 'bd', 'be', 'bf',
                          'cd', 'ce', 'cf'], cross('abc', 'def'))

    def test_box(self):
        self.assertEqual(['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9',
                          'B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B9',
                          'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
                          'D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8', 'D9',
                          'E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8', 'E9', 
                          'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8', 'F9', 
                          'G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8', 'G9', 
                          'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 
                          'I1', 'I2', 'I3', 'I4', 'I5', 'I6', 'I7', 'I8', 'I9'], BOXES)                         
    def test_grid(self):
        self.assertEqual(display(grid_values2('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')),display(grid_values('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')))
    def test_possibilites(self):
        self.assertEqual(display(grid_possibilites('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')),display(grid_possibilites_udacity('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..')))
    def test_eliminate(self):
        self.assertEqual(display(eliminate(grid_possibilites('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))),display(eliminate_udacity(grid_possibilites_udacity('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))))
    def test_eliminate(self):
        self.assertEqual(display(only_choice(grid_possibilites('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))),display(eliminate_udacity(grid_possibilites_udacity('..3.2.6..9..3.5..1..18.64....81.29..7.......8..67.82....26.95..8..2.3..9..5.1.3..'))))

if __name__ == '__main__':
    unittest.main()
# Newline at end of file
