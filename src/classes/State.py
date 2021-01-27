from .Distance import Distance
from .Goal import Goal


class State:
    '''
        Class handles all state changes
        e.g. moves
    '''

    def __init__(self, puzzle, size):
        self.puzzle = puzzle
        self.size = size
        self.goal = Goal(size)
        self.g = 0  # move count
        self.h = Distance(puzzle, self.goal.puzzle).d
        self.f = self.g + self.h

    def _getZeroCoords(self, puzzle):
        '''
            Function returns coordinates of the blank tile
            in the given puzzle
        '''
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if puzzle[i][j] == 0:
                    return i, j

    def _checkMove(self, direction, x, y):
        '''
            Utility function to check if move is possible
        '''
        if direction == 'R':
            if y - 1 < 0:
                raise Exception('Invalid move')
        if direction == 'L':
            if y + 1 >= self.size:
                raise Exception('Invalid move')
        if direction == 'D':
            if x - 1 < 0:
                raise Exception('Invalid move')
        if direction == 'U':
            if x + 1 >= self.size:
                raise Exception('Invalid move')

    def _moveRight(self):
        x, y = self._getZeroCoords(self.puzzle)
        self._checkMove('R', x, y)
        temp = self.puzzle[x][y - 1]
        self.puzzle[x][y - 1] = self.puzzle[x][y]
        self.puzzle[x][y] = temp

    def _moveLeft(self):
        x, y = self._getZeroCoords(self.puzzle)
        self._checkMove('L', x, y)
        temp = self.puzzle[x][y - 1]
        self.puzzle[x][y - 1] = self.puzzle[x][y]
        self.puzzle[x][y] = temp

    def _moveDown(self):
        x, y = self._getZeroCoords(self.puzzle)
        self._checkMove('D', x, y)
        temp = self.puzzle[x - 1][y]
        self.puzzle[x - 1][y] = self.puzzle[x][y]
        self.puzzle[x][y] = temp

    def _moveUp(self):
        x, y = self._getZeroCoords(self.puzzle)
        self._checkMove('U', x, y)
        temp = self.puzzle[x + 1][y]
        self.puzzle[x + 1][y] = self.puzzle[x][y]
        self.puzzle[x][y] = temp

    def move(self, direction):
        '''
            Controller function for the moves
        '''
        if direction == 'R':
            self._moveRight()
        if direction == 'L':
            self._moveLeft()
        if direction == 'D':
            self._moveDown()
        if direction == 'U':
            self._moveUp()
        self.h = Distance(self.puzzle, self.goal.puzzle).d
        self.g += 1
        self.f = self.g + self.h
