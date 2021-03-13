#!/user/bin/env python3
import sys
import argparse
import heapq
from classes.Read import Read
from classes.State import State
from classes.Goal import Goal

TIME = 0
SPACE = 0

def print_usage():
    print("Usage: read.py puzzle")


def getTuple(matrix):
    return tuple(tuple(line) for line in matrix)


def pickSearch(search, node):
    if not search:
        return node.g + node.h
    if search == 'g' or search == 'greedy':
        return node.h
    if search == 'u' or search == 'uniform':
        return node.g


def solver(puzzle, start, size, goal, heuristic, search):
    openset = []
    seenset = {}
    heapq.heappush(openset, (pickSearch(search, start), id(start), start))
    seenset[getTuple(start.puzzle)] = start.g
    global TIME
    global SPACE

    while len(openset) > 0:
        current = heapq.heappop(openset)[2]
        TIME += 1
        if current.h == 0:
            return current

        for matrix in current.getNeighbours():
            move = State(matrix, size, goal, heuristic)
            move.g = current.g + 1
            key = getTuple(move.puzzle)
            if key not in seenset or move.g < seenset[key]:
                if key not in seenset:
                    SPACE += 1
                seenset[key] = move.g
                heapq.heappush(openset, (pickSearch(search, move), id(move), move))
                move.parent = current
    print('Unsolvable')
    return current


def printSolution(solution, start):
    if solution is not start:
        printSolution(solution.parent, start)
    print(f'move #{solution.g}') if solution.g else print('initial state')
    for row in solution.puzzle:
        print(row)
    print()


def checkHeuristic(h):
    if not h:
        if h != 'manhattan' or h != 'euclidean' or h != 'hamming':
            return False
        return False
    return True


if __name__ == "__main__":
    heuristic_desc = 'manhattan (default), hamming, euclidean'
    parser = argparse.ArgumentParser(
        prog='npuzzle', description='Solve N-puzzles')
    parser.add_argument('file', metavar='<inputfile>', action='store',
                        help='Puzzle text file to be solved', type=str)
    parser.add_argument('-d', '--heuristic', action='store',
                        help=heuristic_desc, default=False, type=str)
    parser.add_argument(
        '-s', '--search', choices=['g', 'u', 'greedy', 'uniform'], default=False)
    args = parser.parse_args()
    if checkHeuristic(args.heuristic):
        heuristic = args.heuristic
    else:
        heuristic = 'manhattan'
    data = Read(args.file)
    goal = Goal(data.size)
    state = State(data.puzzle, data.size, goal, heuristic)
    solution = solver(state.puzzle, state, data.size, goal, heuristic, args.search)
    printSolution(solution, state)
    print(f'Solved with {heuristic} distance heuristic')
    print(f'Time complexity: {TIME}\tSpace complexity: {SPACE}')
    print(f'Solved in {solution.g} moves')
