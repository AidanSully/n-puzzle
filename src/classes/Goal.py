class Goal:
    '''
        Class generates a solved puzzle
    '''

    def __init__(self, size):
        self.size = size
        self.puzzle = [[0 for _ in range(self.size)]
                       for __ in range(self.size)]
        self._generate(self.size)

    def _generate(self, n):
        '''
            Function generates and returns a
            solved snail state puzzle
        '''
        inc = 0
        for depth in range(0, int((n + 1) / 2)):
            r = depth
            while r < n - depth:
                inc += 1
                self.puzzle[depth][r] = inc
                r += 1
            d = depth + 1
            while d < n - depth:
                inc += 1
                self.puzzle[d][r - 1] = inc
                d += 1
            l = d - 1
            while l - 1 >= depth:
                inc += 1
                self.puzzle[d - 1][l - 1] = inc
                l -= 1
            u = d - 1
            while u - 1 > depth:
                inc += 1
                self.puzzle[u - 1][l] = inc
                u -= 1
        for row in self.puzzle:
            if (n * n) in row:
                row[row.index(n * n)] = 0
