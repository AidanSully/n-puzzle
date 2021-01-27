class Solvable:
    '''
        Class checks if given npuzzle is solvable
    '''

    def __init__(self, puzzle, puzzle1d, size):
        self.puzzle = puzzle
        self.puzzle1d = puzzle1d
        self.size = size
        self._run()

    def _getInvCount(self):
        '''
            Utility function to count inversions in array puzzle1d[]
            O(n log n) time
        '''

        nbrTiles = (self.size * self.size)
        invCount = 0
        for i in range(nbrTiles - 1):
            for j in range(i + 1, nbrTiles):
                # count pairs (i, j) such that i appears
                # before j, but i > j (aka inversions)
                if (self.puzzle1d[j] and self.puzzle1d[i] and self.puzzle1d[i] > self.puzzle1d[j]):
                    invCount += 1
        return invCount

    def _findZero(self):
        '''
            Utility function to find position of blank tile from bottom
        '''
        for i in range(self.size - 1):
            for j in range(self.size - 1):
                if self.puzzle[i][j] == 0:
                    return self.size - i

    def _isSolvable(self):
        '''
            Function returns True if given N*N - 1 puzzle is solvable
        '''

        invCount = self._getInvCount()
        # If grid is odd, return true if inversion count is even
        if self.size % 2 == 1:
            if invCount % 2 != 0:
                raise Exception('Puzzle is not solvable')
        else:
            zeroPos = self._findZero()
            if zeroPos % 2 == 0:
                if invCount % 2 != 1:
                    raise Exception('Puzzle is not solvable')
            else:
                if invCount % 2 != 0:
                    raise Exception('Puzzle is not solvable')

    def _run(self):
        self._isSolvable()
