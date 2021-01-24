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
