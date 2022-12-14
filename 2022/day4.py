from lib import read_input

def interpret(puzzle_input):
    new_input = []
    for item in puzzle_input:
        a = item.split(',')
        for k in range(len(a)):
            a[k] = a[k].split('-')
            for n in range(len(a[k])):
                a[k][n] = int(a[k][n])
        new_input.append(a)
    return new_input

def contains(puzzle_input):
    # check if left contains right, if right contains left
    contains_sum = 0
    for pair in puzzle_input:
        # left:
        if pair[0][0] >= pair[1][0] and pair[0][1] <= pair[1][1]:
            contains_sum += 1
            continue
        if pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]:
            contains_sum += 1
            continue
    
    return contains_sum

def overlap(puzzle_input):
    overlap_sum = 0
    for pair in puzzle_input:
        if (pair[0][0] >= pair[1][0] and pair[0][0] <= pair[1][1]) or (pair[0][1] <= pair[1][1] and pair[0][1] >= pair[1][0]):
            overlap_sum += 1
            continue
        if (pair[1][0] >= pair[0][0] and pair[1][1] <= pair[0][1]) or (pair[1][1] <= pair[0][1] and pair[1][0] >= pair[0][0]):
            overlap_sum += 1
            continue
    
    return overlap_sum

def overlap_range(puzzle_input):
    overlap_sum = 0
    for pair in puzzle_input:
        right_range = range(pair[1][0], pair[1][1] + 1)
        left_range = range(pair[0][0], pair[0][1] + 1)
        if pair[0][0] in right_range or pair[0][1] in right_range:
            overlap_sum += 1
            continue
        if pair[1][0] in left_range or pair[1][1] in left_range:
            overlap_sum += 1
            continue
    
    return overlap_sum


if __name__ == '__main__':
    pi = read_input('./day4_input.txt')

    input_int = interpret(pi)
    print(contains(input_int))
    print(overlap(input_int))
    print(overlap_range(input_int))