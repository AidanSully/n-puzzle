class VerifyPuzzle:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.error = False
        self.errorMsg = ''

    def _handleError(self, msg):
        self.error = True
        if self.errorMsg == '':
            self.errorMsg = msg

    def _check_numbers(self, size):
        valid_numbers = [n for n in range(size**2)]
        content1d = []
        for row in self.puzzle:
            for n in row:
                content1d.append(n)
        diff = [n for n in valid_numbers if n not in content1d]
        if len(diff) != 0:
            self._handleError('Invalid input, puzzle tile numbers are invalid')

    def _is_valid(self):
        '''Function checks if format is valid
            exits if invalid'''
        if len(self.puzzle[0]) != 1:
            self._handleError(
                'Invalid input, first line should only contain size')
        size = self.puzzle.pop(0)[0]
        if size < 2:
            self._handleError('Invalid input, size cant be < 2')
        print('{} : {}'.format(len(self.puzzle), size))
        if len(self.puzzle) != size:
            self._handleError(
                'Invalid input, given size does not match actual size')
        for row in self.puzzle:
            if len(row) != size:
                self._handleError(
                    'Invalid input, given size does not match actual size')
        self._check_numbers(size)

    def run(self):
        self._is_valid()
