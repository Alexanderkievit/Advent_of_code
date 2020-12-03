input_file = open('Advent_of_code\Day2\input_dag2.txt', "r") 
input = [line.replace('-', ' ').replace(': ', ' ').split(' ') for line in input_file.read().splitlines()]
input_file.close()

def part1(input):
    counter = 0
    for password in input:
        char_count = password[3].count(password[2])
        if int(password[0])<= char_count<= int(password[1]):
            counter += 1
    return counter

def part2(input):
    count = 0
    for password in input:
        l1 = password[3][int(password[0])-1]
        l2 = password[3][int(password[1])-1]
        looking = password[2]
        if (l1 == looking and l2 != looking) or (l1 != looking and l2 == looking):
            count += 1
    return count

print(part1(input))
print(part2(input))