from .Goal import Goal


class Solvable:
    '''
        Class checks if given npuzzle is solvable
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

    def _getInvCount(self, puzzle):
        '''
            Utility function to count inversions in given puzzle
            O(n log n) time
        '''

        nbrTiles = (self.size * self.size)
        invCount = 0
        for i in range(nbrTiles - 1):
            for j in range(i + 1, nbrTiles):
                # count pairs (i, j) such that i appears
                # before j, but i > j (aka inversions)
                if (puzzle[j] and puzzle[i] and puzzle[i] > puzzle[j]):
                    invCount += 1
        return invCount

    def _isSolvable(self):
        '''
            Function returns True if given N*N - 1 puzzle is solvable
        '''

        goal = Goal(self.size)
        puzzle1d = self._convert(self.puzzle)
        goal1d = self._convert(goal.puzzle)
        invPuzzle = self._getInvCount(puzzle1d)
        invGoal = self._getInvCount(goal1d)
        if self.size % 2 == 0:
            invPuzzle += puzzle1d.index(0)
            invGoal += goal1d.index(0)
        if not (invPuzzle % 2 == invGoal % 2):
            raise Exception('Error: puzzle unsolvable')

    def _run(self):
        self._isSolvable()
