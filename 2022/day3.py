import lib
import string

def getPriority():
    ind = 1
    priority_dict = {}
    for i in string.ascii_letters:
        priority_dict[i] = ind
        ind += 1
    
    return priority_dict

def matchPrioritySum(puzzle_input, priority):
    priority_sum = 0
    for sack in puzzle_input:
        a = list(sack[slice(0,len(sack)//2)])
        b = list(sack[slice(len(sack)//2,len(sack))])
        for i in a:
            if i in b:
                priority_sum += priority[i]
                break
    
    return priority_sum

def badgeGroups(puzzle_input):
    badge_groups = []
    for i in range(0, len(puzzle_input), 3):
        badge_groups.append([puzzle_input[i], puzzle_input[i+1], puzzle_input[i+2]])
    return badge_groups

def bgPrioritySum(badge_groups, priority):
    bg_priority_sum = 0
    for group in badge_groups:
        for item in group[0]:
            if item in group[1] and item in group[2]:
                bg_priority_sum += priority[item]
                break
    
    return bg_priority_sum


if __name__ == '__main__':
    pi = lib.read_input('./day3_input.txt')
    pd = getPriority()
    print(matchPrioritySum(pi, pd))
    bg = badgeGroups(pi)
    print(bgPrioritySum(bg, pd))