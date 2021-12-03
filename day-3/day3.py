def clean_input(filepath):
    result_list = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                result_list.append(line)
    return result_list


def part_one(values_list):
    gamma, epsilon = "", ""
    for pos_index in range(0, len(values_list[0])):
        zeros, ones = 0, 0
        for line in values_list:
            if line[pos_index] == "1":
                ones += 1
            else:
                zeros += 1
        if ones > zeros:
            gamma += "1"
            epsilon += "0"
        else:
            gamma += "0"
            epsilon += "1"
    return int(gamma, 2)*int(epsilon, 2)


def calculate_oxygen(values):
    pos_index = 0
    while len(values) > 1:
        zeros, ones = 0, 0
        for value in values:
            if value[pos_index] == "1":
                ones += 1
            else:
                zeros += 1
        if ones >= zeros:
            values = list(
                filter(lambda value: value[pos_index] == "1", values))
        else:
            values = list(
                filter(lambda value: value[pos_index] == "0", values))
        pos_index += 1
    return values[0]


def calculate_co2(values):
    pos_index = 0
    while len(values) > 1:
        zeros, ones = 0, 0
        for value in values:
            if value[pos_index] == "1":
                ones += 1
            else:
                zeros += 1
        if ones < zeros:
            values = list(
                filter(lambda value: value[pos_index] == "1", values))
        else:
            values = list(
                filter(lambda value: value[pos_index] == "0", values))
        pos_index += 1
    return values[0]


def part_two(values):
    oxygen = calculate_oxygen(values)
    co2 = calculate_co2(values)
    return int(oxygen, 2)*int(co2, 2)


if __name__ == '__main__':
    values_list = clean_input('./input.txt')
    print("The answer for part one is " + str(part_one(values_list)))
    print("The answer for part two is " + str(part_two(values_list)))
