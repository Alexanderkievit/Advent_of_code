input_file = open('Advent_of_code\Day3\input.txt', 'r')
input = input_file.readlines()
input = [line.strip() for line in input]

def part1(input):
    counter = 0
    row, kolom = 0,0
    while row+1 < len(input):
        row += 1
        kolom += 3
        a = input[row][kolom % len(input[row])]

        if a == '#':
            counter += 1 
    return counter

def part2(input):
    slopes = [(1,1), (3,1), (5, 1), (7, 1), (1, 2)]
    total = 1

    for slope in slopes:

        counter = 0
        row, kolom = 0,0

        while row+1 < len(input):
            row += slope[1]
            kolom += slope[0]
            a = input[row][kolom % len(input[row])]
            if a == '#':
                counter += 1

        total *= counter

    return total
print(part1(input))
print(part2(input))