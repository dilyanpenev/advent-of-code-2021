def clean_input(filepath):
    result_list = []
    with open(filepath) as f:
        for line in f:
            line = line.strip().split()
            if line:
                result_list.append(line)
    return result_list


def part_one(steps_list):
    horizontal, depth = 0, 0
    for step in steps_list:
        if step[0] == "forward":
            horizontal += int(step[1])
        elif step[0] == "down":
            depth += int(step[1])
        elif step[0] == "up":
            depth -= int(step[1])
    return horizontal*depth


def part_two(steps_list):
    horizontal, depth, aim = 0, 0, 0
    for step in steps_list:
        if step[0] == "forward":
            horizontal += int(step[1])
            depth += int(step[1])*aim
        elif step[0] == "down":
            aim += int(step[1])
        elif step[0] == "up":
            aim -= int(step[1])
    return horizontal*depth


if __name__ == '__main__':
    steps_list = clean_input('./input.txt')
    print("The answer for part one is " + str(part_one(steps_list)))
    print("The answer for part two is " + str(part_two(steps_list)))
