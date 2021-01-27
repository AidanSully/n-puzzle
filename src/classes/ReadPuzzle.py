from .ValidPuzzle import ValidPuzzle
from .SolvablePuzzle import SolvablePuzzle


class ReadPuzzle:
    '''
        Class handles reading puzzle input
    '''

    def __init__(self, file):
        self.file = file
        self.size, self.puzzle = self._run()

    def _readFile(self):
        '''
            Function reads file
            cleans comments and empty lines
            returns cleaned content of the file
        '''
        f = open(self.file, "r")
        content = f.readlines()
        f.close()
        content = [line.strip().split('#')[0] for line in content]  # Comment
        content = [line for line in content if len(line) > 0]  # Empty line
        return content

    def _convert(self, content):
        '''
            Function checks if all input are digits
            and adds the input to data as a 2d array 
            e.g. size = 3 | [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
            returns the puzzle data array
        '''
        data = []
        for line in content:
            row = []
            for n in line.split(' '):
                if not n.isdigit():
                    if not n.isdigit():
                        raise Exception(
                            'Error: Invalid input, must all be numeric values\n')
                row.append(int(n))
            data.append(row)
        return (data)

    def _run(self):
        '''
            Main parsing function
            calls other parse functions
            returns valid puzzle and size
        '''
        puzzle = self._convert(self._readFile())
        size = puzzle[0][0]
        valid = ValidPuzzle(puzzle, size)
        SolvablePuzzle(puzzle, valid.puzzle1d, size)
        return (size, puzzle)
