class VerifyPuzzle:
    def __init__(self, puzzle, size):
        self.puzzle = puzzle
        self.size = size
        self.error = False
        self.errorMsg = ''
        self.puzzle1d = []
        self.run()

    def _handleError(self, msg):
        self.error = True
        if self.errorMsg == '':
            self.errorMsg = msg

    def _checkNumbers(self, size):
        '''Function checks is numbers in puzzle are valid'''

        valid_numbers = [n for n in range(size**2)]
        for row in self.puzzle:
            for n in row:
                self.puzzle1d.append(n)
        diff = [n for n in valid_numbers if n not in self.puzzle1d]
        if len(diff) != 0:
            self._handleError('Invalid input, puzzle tile numbers are invalid')

    def _isValid(self):
        '''Function checks if format is valid
            exits if invalid'''

        if len(self.puzzle[0]) != 1:
            self._handleError(
                'Invalid input, first line should only contain size')
        self.size = self.puzzle.pop(0)[0]
        if self.size < 2:
            self._handleError('Invalid input, size cant be < 2')
        if len(self.puzzle) != self.size:
            self._handleError(
                'Invalid input, given size does not match actual size')
        for row in self.puzzle:
            if len(row) != self.size:
                self._handleError(
                    'Invalid input, given size does not match actual size')
        self._checkNumbers(self.size)

    def _getInvCount(self):
        '''Utility function to count inversions in array puzzle1d[]
            O(n log n) time'''

        nbrTiles = (self.size * self.size)
        invCount = 0
        for i in range(nbrTiles - 1):
            for j in range(i + 1, nbrTiles):
                # count pairs (i, j) such that i appears
                # before j, but i > j (aka inversions)
                if (self.puzzle1d[j] and self.puzzle1d[i] and self.puzzle1d[i] > self.puzzle1d[j]):
                    invCount += 1
        return invCount

    def _findEmpty(self):
        '''Utility function to find position of blank tile from bottom'''
        for i in range(self.size - 1):
            for j in range(self.size - 1):
                if self.puzzle[i][j] == 0:
                    return self.size - i

    def _isSolvable(self):
        '''Function returns True if given N*N - 1 puzzle is solvable'''

        invCount = self._getInvCount()
        # If grid is odd, return true if inversion count is even
        if self.size % 2 == 1:
            if invCount % 2 != 0:
                self._handleError('Puzzle is not solvable')
        else:
            emptyPos = self._findEmpty()
            if emptyPos % 2 == 0:
                if invCount % 2 != 1:
                    self._handleError('Puzzle is not solvable')
            else:
                if invCount % 2 != 0:
                    self._handleError('Puzzle is not solvable')

    def run(self):
        self._isValid()
        self._isSolvable()
