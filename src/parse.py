#!/user/bin/env python3
import sys


def print_usage():
    print("Usage: read.py puzzle")


def read_file(file):
    '''Function reads file
        cleans comments and empty lines
        returns cleaned content of the file'''
    f = open(file, "r")
    content = f.readlines()
    f.close()
    content = [line.strip().split('#')[0] for line in content]  # Comment
    content = [line for line in content if len(line) > 0]  # Empty line
    return content


def print_error(msg):
    print('Error: {}'.format(msg))
    exit()

def check_numbers(content, size):
    valid_numbers = [n for n in range(size**2)]
    content1d = []
    for row in content:
        for n in row:
            content1d.append(n)
    diff = [n for n in valid_numbers if n not in content1d]
    if len(diff) != 0:
        print_error('Invalid input, puzzle tile numbers are invalid')

def is_valid(content):
    '''Function checks if format is valid
        exits if invalid'''
    if len(content[0]) != 1:
        print_error('Invalid input, first line should only contain size')
    size = content.pop(0)[0]
    if size < 2:
        print_error('Invalid input, size cant be < 2')
    if len(content) != size:
        print_error('Invalid input, given size does not match actual size')
    for row in content:
        if len(row) != size:
            print_error('Invalid input, given size does not match actual size')
    check_numbers(content, size)


def parse_input(content):
    '''Function checks if content is numeric
        and parses the content into data
        returns the puzzle data'''
    data = []
    for line in content:
        row = []
        for n in line.split(' '):
            if not n.isdigit():
                print('Error: Invalid input, must all be numeric values')
                print_error('{} is not a numeric value'.format(n))
            row.append(int(n))
        data.append(row)
    return (data)


def parse(file):
    '''Main parsing function
        calls other parse functions
        returns valid puzzle and size'''
    content = read_file(file)
    puzzle = parse_input(content)
    size = puzzle[0][0]
    is_valid(puzzle)
    return (puzzle, size)


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print_usage()
        exit()
    puzzle, size = parse(sys.argv[1])
    print(size)
    print(puzzle)
