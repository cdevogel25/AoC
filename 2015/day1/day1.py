f = open('./day1.txt', 'r')
floor = 0
string = f.read()
for i, c in enumerate(string):
    if(c == '('):
        floor += 1
    elif(c == ')'):
        floor -= 1

    if(floor < 0):
        print i
        break

print floor
