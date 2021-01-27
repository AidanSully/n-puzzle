#!/user/bin/env python3
import sys
from classes.Read import Read
from classes.State import State


def print_usage():
    print("Usage: read.py puzzle")


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print_usage()
        exit()
    data = Read(sys.argv[1])
    state = State(data.puzzle, data.size)
    for row in state.puzzle:
        print(row)
    print('\ng: {}\th: {}\tf: {}\n'.format(state.g, state.h, state.f))
    state.move('R')
    for row in state.puzzle:
        print(row)
    print('\ng: {}\th: {}\tf: {}\n'.format(state.g, state.h, state.f))
    state.move('L')
    for row in state.puzzle:
        print(row)
    print('\ng: {}\th: {}\tf: {}\n'.format(state.g, state.h, state.f))
    state.move('D')
    for row in state.puzzle:
        print(row)
    print('\ng: {}\th: {}\tf: {}\n'.format(state.g, state.h, state.f))
    state.move('U')
    for row in state.puzzle:
        print(row)
    print('\ng: {}\th: {}\tf: {}\n'.format(state.g, state.h, state.f))
