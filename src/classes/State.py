import copy
from .Distance import Distance
from .Goal import Goal


class State:
    '''
        Class handles all state changes
        e.g. moves
    '''

    def __init__(self, puzzle, size, goal, heuristic):
        self.puzzle = puzzle
        self.size = size
        self.goal = goal
        self.parent = 0
        self.g = 0  # move count
        self.h = Distance(puzzle, goal.puzzle, heuristic).d

    def _getZeroCoords(self, puzzle):
        '''
            Function returns coordinates of the blank tile
            in the given puzzle
        '''
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if puzzle[i][j] == 0:
                    return i, j

    def _checkMove(self, x, y):
        '''
            Utility function to check if move is possible
        '''
        coords = []
        if x - 1 >= 0:
            coords.append((x - 1, y))
        if y - 1 >= 0:
            coords.append((x, y - 1))
        if y + 1 < self.size:
            coords.append((x, y + 1))
        if x + 1 < self.size:
            coords.append((x + 1, y))
        return coords

    def getNeighbours(self):
        x, y = self._getZeroCoords(self.puzzle)
        coords = self._checkMove(x, y)
        states = [copy.deepcopy(self.puzzle) for _ in coords]
        for i in range(len(coords)):
            x2, y2 = coords[i]
            states[i][x][y], states[i][x2][y2] = self.puzzle[x2][y2], self.puzzle[x][y]
        return states
