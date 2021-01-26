class Distance:
    '''
        Class returns the distance using different heuristics
    '''

    def __init__(self, puzzle, goal, heuristic='manhattan'):
        self.heuristic = heuristic
        self.puzzle = puzzle
        self.goal = goal
        self.puzzle1d = self._get1d(self.puzzle)
        self.goal1d = self._get1d(self.goal)
        self.d = self._getDistance()

    def _get1d(self, puzzle):
        puzzle1d = []
        for row in puzzle:
            for n in row:
                puzzle1d.append(n)
        return puzzle1d

    def _getCoords(self, puzzle, value):
        '''Function returns coordinates of the given value
            in the given puzzle
            '''
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if value == puzzle[i][j]:
                    return i, j

    def _getDistance(self):
        '''Controller function for 
            getting and returning the distance
        '''
        if (self.heuristic.lower() == 'hamming'):
            return self._hamming(self.puzzle1d,  self.goal1d)
        if (self.heuristic.lower() == 'manhattan'):
            return self._manhattan(self.puzzle, self.goal)
        if (self.heuristic.lower() == 'linear'):
            return self._linear()

    def _manhattan(self, puzzle, goal):
        '''Function calculates and returns the 
            Manhattan distance for each tile summed up'''
        d = 0
        for x in range(len(puzzle)):
            for y in range(len(puzzle[x])):
                if puzzle[x][y] and puzzle[x][y] != goal[x][y]:
                    goalX, goalY = self._getCoords(goal, puzzle[x][y])
                    d += abs((x + y) - (goalX + goalY))
        return d

    def _countConflicts(self):
        pass

    def _linear(self):
        '''Function calculates and returns the
            Linear Conflict + Manhattan Distance
        '''
        d = self._manhattan(self.puzzle, self.goal)
        # TODO
        # Add linear conflict count
        return d

    def _hamming(self, puzzle1d, goal1d):
        '''Function calculates and returns the 
            Hamming distance for each tile summed up'''
        d = 0
        for i in range(len(puzzle1d)):
            if puzzle1d and puzzle1d[i] != goal1d[i]:
                d += 1
        return d
