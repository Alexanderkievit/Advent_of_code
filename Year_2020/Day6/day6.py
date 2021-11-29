with open("input.txt") as file:
    data = file.readlines()
    data = [line.strip() for line in data]


# Part 1
def unique_item(response):
    items = []
    # print(response)
    for item in response:
        if item not in items:
            items.append(item)
    return len(items)

current_responese = ""
sum = 0
for line in data:
    if line != "":
        current_responese += line

    else:
        sum += unique_item(current_responese)
        current_responese = ""

sum += unique_item(current_responese)
print(sum)

# Part 2
def find_letters(input):
    sum_input = len(input)
    letters = []
    zin = ""
    for char in input[0]:
        in_all_line = True
        for line in input:
            if char not in line:
                in_all_line = False

        if in_all_line and char not in letters:
            letters.append(char)
    return len(letters)


list_response = []
sum = 0
for line in data:
    if line != "":
        list_response.append(line)
    else:
        sum += find_letters(list_response)
        list_response = []
sum += find_letters(list_response)
print(sum)
