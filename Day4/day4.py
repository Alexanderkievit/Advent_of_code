input_file = open('Advent_of_code\Day4\input.txt', 'r')
input = input_file.readlines()
input = [line.strip() for line in input]

goede_passpoorten = []
def part1(input):
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    def is_valid_passport(pp):
        for field in fields:
            if field not in pp:
                return False
        return True

    valid_count = 0

    current_passport = ''
    for line in input:
        if line != '':
            current_passport += ' ' + line

        else:
            if is_valid_passport(current_passport):
                goede_passpoorten.append(current_passport)
                valid_count += 1
            
            current_passport = ''
    if is_valid_passport(current_passport):
        goede_passpoorten.append(current_passport)
        valid_count += 1
    return valid_count

print(part1(input))


def part2(input):
    counter = 0

    def is_valid_byr(byr):
        byr = int(byr)
        if byr < 1920 or byr > 2002:
            return False
        return True

    def is_valid_iyr(iyr):
        iyr = int(iyr)
        if iyr < 2010 or iyr > 2020:
            return False
        return True
 
    def is_valid_eyr(eyr):
        eyr = int(eyr)
        if eyr < 2020 or eyr > 2030:
            return False
        return True

    def is_valid_hgt(hgt):
        units = hgt[-2:]

        if units not in ['in', 'cm']:
            return False
            
        hgt = int(hgt[:-2])
        if units == 'in':
            if hgt < 59 or hgt > 76:
                return False
        elif units == 'cm':
            if hgt < 150 or hgt > 193:
                return False
        return True   

    def is_valid_hcl(hcl):
        if hcl[0] != '#': return False
        
        if len(hcl[1:]) != 6: return False
        
        return True

    def is_valid_ecl(ecl):
        colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if ecl not in colors:
            return False
        return True

    def is_valid_pid(pid):
        if len(pid) != 9:
            return False
        return True

    def has_valid_data(passport):
        passport = passport.split()
        data = {}

        for item in passport:
            key = item[:3]
            value = item[4:]
            data[key] = value
        
        if not is_valid_byr(data['byr']):
            return False
        
        if not is_valid_eyr(data['eyr']):
            return False

        if not is_valid_iyr(data['iyr']):
            return False

        if not is_valid_hgt(data['hgt']):
            return False

        if not is_valid_hcl(data['hcl']):
            return False

        if not is_valid_ecl(data['ecl']):
            return False

        if not is_valid_pid(data['pid']):
            return False

        return True

    for pp in input:
        if has_valid_data(pp):
            counter += 1
    return counter

print(part2(goede_passpoorten))