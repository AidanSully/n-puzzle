#!/user/bin/env python3
import sys
from Modules.parser import Parser
from Modules.verifyPuzzle import VerifyPuzzle


def print_usage():
    print("Usage: read.py puzzle")


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print_usage()
        exit()
    puzzle = Parser(sys.argv[1])
    if (puzzle.error == True):
        print(puzzle.errorMsg)
        exit()
    verifier = VerifyPuzzle(puzzle.puzzle, puzzle.size)
    if (verifier.error == True):
        print(verifier.errorMsg)
        exit()
    print(puzzle.size)
    print(puzzle.puzzle)
