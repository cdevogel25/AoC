s = '^>v<'
ypos = 0
xpos = 0
houses = [[]]
for i in s:
    if i == '^':
        ypos += 1
    elif i == 'v':
        ypos -= 1
    elif i == '>':
        xpos += 1
    elif i == '<':
        xpos -= 1

print x, y
