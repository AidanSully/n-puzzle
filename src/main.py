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
    parser = Parser(sys.argv[1])
    puzzle, size = parser.run()
    if (parser.error == True):
        print(parser.errorMsg)
        exit()
    verifier = VerifyPuzzle(puzzle)
    verifier.run()
    if (verifier.error == True):
        print(verifier.errorMsg)
        exit()
    print(size)
    print(puzzle)
