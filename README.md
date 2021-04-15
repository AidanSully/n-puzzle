# N-Puzzle
## Aidan Sullivan
________________________

### A Python program that solves an n-puzzle
See: https://en.wikipedia.org/wiki/15_puzzle

Size of the puzzle is n*n

![npuzzle.PNG](https://github.com/AidanSully/n-puzzle/blob/master/resources/npuzzle.PNG)

### Usage
```usage: npuzzle [-h] [-d HEURISTIC] [-s {g,u,greedy,uniform}] <inputfile>

Solve N-puzzles

positional arguments:
  <inputfile>           Puzzle text file to be solved

optional arguments:
  -h, --help            show this help message and exit
  -d HEURISTIC, --heuristic HEURISTIC
                        manhattan (default), hamming, euclidean
  -s {g,u,greedy,uniform}, --search {g,u,greedy,uniform}
```

### Heuristics
#### Manhattan distance
```
The Manhattan distance between two points x = (x1, x2, …, xn) and y = (y1, y2, …, yn) in n-dimensional space is the sum of the distances in each dimension.
```
#### Hamming distance
```
Hamming distance is a metric for comparing two binary data strings. In our case it would be current state compared to solved state. h = number of misplaced tiles
```
#### Euclidean distance
```
The Euclidean distance between two points in either the plane or 3-dimensional space measures the length of a segment connecting the two points. It is the most obvious way of representing distance between two points.

The Pythagorean Theorem can be used to calculate the distance between two points.
```