#!/user/bin/env python3
import sys
from Modules.parser import Parser
from Modules.verifyPuzzle import VerifyPuzzle
from Modules.solution import Solution
from Modules.distance import Distance


def print_usage():
    print("Usage: read.py puzzle")


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print_usage()
        exit()
    state = Parser(sys.argv[1])
    if (state.error == True):
        print(state.errorMsg)
        exit()
    verifier = VerifyPuzzle(state.puzzle, state.size)
    if (verifier.error == True):
        print(verifier.errorMsg)
        exit()
    print('size: {}\n'.format(state.size))
    print('Initial state:\n')
    for row in state.puzzle:
        print(row)
    print()
    goal = Solution(state.size)
    print('Goal state:\n')
    for row in goal.puzzle:
        print(row)
    print()
    h = Distance(state.puzzle, goal.puzzle)
    print('Heuristic distance: {}'.format(h.d))
    state.move(5, 'R')
    if (state.error == True):
        print(state.errorMsg)
        exit()
    for row in state.puzzle:
        print(row)
    print()
    state.move(5, 'L')
    if (state.error == True):
        print(state.errorMsg)
        exit()
    for row in state.puzzle:
        print(row)
    print()
    state.move(2, 'D')
    if (state.error == True):
        print(state.errorMsg)
        exit()
    for row in state.puzzle:
        print(row)
    print()
    state.move(2, 'U')
    if (state.error == True):
        print(state.errorMsg)
        exit()
    for row in state.puzzle:
        print(row)
    print()
