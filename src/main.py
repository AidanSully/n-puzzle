#!/user/bin/env python3
import sys
from classes.ReadPuzzle import ReadPuzzle
from classes.State import State



def print_usage():
    print("Usage: read.py puzzle")


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print_usage()
        exit()
    data = ReadPuzzle(sys.argv[1])
    state = State(data.puzzle, data.size)
    for row in state.puzzle:
        print(row)
    print('\nh: {}\n'.format(state.h))
    state.move('R')
    for row in state.puzzle:
        print(row)
    print('\nh: {}\n'.format(state.h))
    state.move('L')
    for row in state.puzzle:
        print(row)
    print('\nh: {}\n'.format(state.h))
    state.move('D')
    for row in state.puzzle:
        print(row)
    print('\nh: {}\n'.format(state.h))
    state.move('U')
    for row in state.puzzle:
        print(row)
    print('\nh: {}\n'.format(state.h))

