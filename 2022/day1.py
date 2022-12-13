def read_input(filename):
    puzzle_input = []
    with open(filename) as f:
        line = f.readline().rstrip()
        while line:
            puzzle_input.append(line.strip())
            line = f.readline()
    
    return puzzle_input

def input_s2i(s):
    s2i_input = []
    elf = []
    for entry in s:
        if entry == '':
            s2i_input.append(elf)
            elf = []
        else:
            elf.append(int(entry))
    
    return s2i_input

def max_elf(elves):
    elf_sums = []
    cal_max = 0
    for i in range(len(elves)):
        s = sum(elves[i])
        if s > cal_max:
            cal_max = s
        elf_sums.append(sum(elves[i]))
    
    return elf_sums, cal_max

def maxN(elements, n):
    return sorted(elements, reverse=True)[:n]


if __name__ == '__main__':
    elves = input_s2i(read_input('.\day1_input.txt'))
    elf_sums, cal_max = max_elf(elves)
    max3 = maxN(elf_sums, 3)
    print(cal_max)
    print(sum(max3))
