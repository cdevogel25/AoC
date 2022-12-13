from lib import read_input

def interpret(puzzle_input):
    new_input = []
    for item in puzzle_input:
        a = item.split(',')
        print(a)
        for k in range(len(a)):
            a[k] = a[k].split('-')
            for n in range(len(a[k])):
                a[k][n] = int(a[k][n])
        new_input.append(a)
    print(new_input)

if __name__ == '__main__':
    pi = read_input('./day4_input.txt')

    interpret(pi)