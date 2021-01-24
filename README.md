# N-Puzzle
## Aidan Sullivan
________________________

### A Python program that solves an n-puzzle
See: https://en.wikipedia.org/wiki/15_puzzle
Size of the puzzle is n*n

### Usage
$ python3 main.py [puzzle]

puzzle is in a file with the following format:
`3<br>
4 7 6<br>
3 0 1<br>
2 5 8<br>
`

## Todo
- Implement hueristic functions which include [resource](https://algorithmsinsight.wordpress.com/graph-theory-2/a-star-in-general/implementing-a-star-to-solve-n-puzzle/):
    - Hamming distance/Misplaced tiles (Slowest)
    - Manhattan Distance/Taxicab geometry (Slow for higher values)
    - Linear Conflict + Manhattan Distance/Taxicab geometry
- Implement A* algorithm