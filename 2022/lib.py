def read_input(filename):
    puzzle_input = []
    with open(filename) as f:
        line = f.readline().rstrip()
        while line:
            puzzle_input.append(line.strip())
            line = f.readline()
    
    return puzzle_input