class Valid:
    '''
        Class checks npuzzle for valid input
    '''

    def __init__(self, puzzle, size):
        self.puzzle = puzzle
        self.size = size
        self._run()

    def _convert(self, puzzle):
        puzzleList = []
        for row in puzzle:
            for n in row:
                puzzleList.append(n)
        return puzzleList

    def _checkNumbers(self, size):
        '''
            Function checks if numbers in puzzle are valid
            and creates 1d array from 2d array
        '''

        valid_numbers = [n for n in range(size**2)]
        puzzle1d = self._convert(self.puzzle)
        diff = [n for n in valid_numbers if n not in puzzle1d]
        if len(diff) != 0:
            raise Exception('Error: Invalid input, puzzle tile numbers are invalid')

    def _isValid(self):
        '''
            Function checks if format is valid
        '''

        if len(self.puzzle[0]) != 1:
            raise Exception(
                'Error: Invalid input, first line should only contain size')
        self.size = self.puzzle.pop(0)[0]
        if self.size < 2:
            raise Exception('Error Invalid input, size cant be < 2')
        if len(self.puzzle) != self.size:
            raise Exception(
                'Error: Invalid input, given size does not match actual size')
        for row in self.puzzle:
            if len(row) != self.size:
                raise Exception(
                    'Error: Invalid input, given size does not match actual size')
        self._checkNumbers(self.size)

    def _run(self):
        self._isValid()
