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
        print(self.d)

    def _get1d(self, puzzle):
        puzzle1d = []
        for row in puzzle:
            for n in row:
                puzzle1d.append(n)
        return puzzle1d

    def _getDistance(self):
        if (self.heuristic.lower() == 'hamming'):
            return self._hamming()
        if (self.heuristic.lower() == 'manhattan'):
            return self._manhattan()
        if (self.heuristic.lower() == 'linear'):
            return self._linear()

    def _manhattan(self):
        pass

    def _linear(self):
        pass

    def _hamming(self):
        '''Function calculates and returns the 
            Hamming distance for each tile summed up'''
        d = 0
        for i in range(len(self.puzzle1d)):
            if self.puzzle1d[i] != self.goal1d[i]:
                d += 1
        return d
