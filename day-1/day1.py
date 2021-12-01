def clean_input(filepath):
    result_list = []
    with open(filepath) as f:
        for line in f:
            line = line.strip()
            if line:
                result_list.append(int(line))
    return result_list


def part_one(values_list):
    num_larger = 0
    for i in range(1, len(values_list)):
        if values_list[i] > values_list[i-1]:
            num_larger += 1
    return num_larger


def part_two(values_list):
    num_larger = 0
    for i in range(0, len(values_list)-3):
        if values_list[i] < values_list[i+3]:
            num_larger += 1
    return num_larger


if __name__ == '__main__':
    depths_list = clean_input('./input.txt')
    print("The answer for part one is " + str(part_one(depths_list)))
    print("The answer for part two is " + str(part_two(depths_list)))
