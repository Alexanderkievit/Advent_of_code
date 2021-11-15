# Part 1
def part1_row(passport):
    lower = 0
    upper = 127
    for i in range(6):
        half = (upper + lower) // 2
        if passport[i] == "F":
            upper = half
        elif passport[i] == "B":
            lower = half + 1
    if passport[6] == "F":
        return lower
    else:
        return upper


def part1_col(passport):
    lower = 0
    upper = 7
    for i in range(2):
        half = (upper + lower) // 2
        if passport[i] == "L":
            upper = half
        elif passport[i] == "R":
            lower = half + 1

    if passport[2] == "L":
        return lower
    else:
        return upper

all_numbers = []
grootste = 0
with open("input.txt") as file:
    input = file.readlines()
    input = [line.strip() for line in input]

    for passport in input:
        row = part1_row(passport[:7])
        col = part1_col(passport[7:])

        seat = (row * 8) + col
        all_numbers.append(seat)
        if seat > grootste:
            grootste = seat

# Part 2
for id in all_numbers:
    if id+1 not in all_numbers and id+2 in all_numbers:
        missing_seat = id+1
print(missing_seat)

