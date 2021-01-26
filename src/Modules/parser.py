class Parser:
    '''
        Class handles reading and parsing files for npuzzle
    '''

    def __init__(self, file):
        self.file = file
        self.error = False
        self.errorMsg = ''
        self._run()

    def _handleError(self, msg):
        self.error = True
        if self.errorMsg == '':
            self.errorMsg = msg

    def _read_file(self):
        '''Function reads file
            cleans comments and empty lines
            returns cleaned content of the file'''
        f = open(self.file, "r")
        content = f.readlines()
        f.close()
        content = [line.strip().split('#')[0] for line in content]  # Comment
        content = [line for line in content if len(line) > 0]  # Empty line
        return content

    def _convert(self):
        '''Function checks if all input are digits
            and adds the input to data as a 2d array 
            e.g. size = 3 | [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
            returns the puzzle data array'''
        data = []
        for line in self.content:
            row = []
            for n in line.split(' '):
                if not n.isdigit():
                    self._handleError(
                        'Error: Invalid input, must all be numeric values\n\'{}\' is not a numeric value'.format(n))
                    break
                row.append(int(n))
            data.append(row)
        return (data)

    def _run(self):
        '''Main parsing function
            calls other parse functions
            returns valid puzzle and size'''
        self.content = self._read_file()
        self.puzzle = self._convert()
        self.size = self.puzzle[0][0]

    def _getCoords(self, puzzle, value):
        '''Function returns coordinates of the given value
            in the given puzzle
            '''
        for i in range(len(puzzle)):
            for j in range(len(puzzle[i])):
                if value == puzzle[i][j]:
                    return i, j

    def _checkZero(self, puzzle, x, y, direction):
        if direction == 'R':
            if y + 1 > self.size or puzzle[x][y + 1]:
                return False
        if direction == 'L':
            if y - 1 < 0 or puzzle[x][y - 1]:
                return False
        if direction == 'D':
            if x + 1 > self.size or puzzle[x + 1][y]:
                return False
        if direction == 'U':
            if x - 1 < 0 or puzzle[x - 1][y]:
                return False
        return True

    def _moveRight(self, value):
        x, y = self._getCoords(self.puzzle, value)
        if self._checkZero(self.puzzle, x, y, 'R') == False:
            self._handleError('Invalid move')
            return
        temp = self.puzzle[x][y + 1]
        self.puzzle[x][y + 1] = self.puzzle[x][y]
        self.puzzle[x][y] = temp
    
    def _moveLeft(self, value):
        x, y = self._getCoords(self.puzzle, value)
        if self._checkZero(self.puzzle, x, y, 'L') == False:
            self._handleError('Invalid move')
            return
        temp = self.puzzle[x][y - 1]
        self.puzzle[x][y - 1] = self.puzzle[x][y]
        self.puzzle[x][y] = temp
    
    def _moveDown(self, value):
        x, y = self._getCoords(self.puzzle, value)
        if self._checkZero(self.puzzle, x, y, 'D') == False:
            self._handleError('Invalid move')
            return
        temp = self.puzzle[x + 1][y]
        self.puzzle[x + 1][y] = self.puzzle[x][y]
        self.puzzle[x][y] = temp
    
    def _moveUp(self, value):
        x, y = self._getCoords(self.puzzle, value)
        if self._checkZero(self.puzzle, x, y, 'U') == False:
            self._handleError('Invalid move')
            return
        temp = self.puzzle[x - 1][y]
        self.puzzle[x - 1][y] = self.puzzle[x][y]
        self.puzzle[x][y] = temp

    def move(self, value, direction):
        if direction == 'R':
            self._moveRight(value)
        if direction == 'L':
            self._moveLeft(value)
        if direction == 'D':
            self._moveDown(value)
        if direction == 'U':
            self._moveUp(value)
