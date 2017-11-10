f = open('./day3.txt', 'r')
s = f.readlines()[0]
#print s
ypos = 0
ypos_r = 0
xpos = 0
xpos_r = 0
positions = {}
for i in s[0::2]:
    if i == '^':
        ypos += 1
    elif i == 'v':
        ypos -= 1
    elif i == '>':
        xpos += 1
    elif i == '<':
        xpos -= 1
    ps = str(xpos) + ',' + str(ypos)
    if ps not in list(positions.keys()):
        positions[ps] = 1
    elif ps in list(positions.keys()):
        positions[ps] += 1;

for i in s[1::2]:
    if i == '^':
        ypos_r += 1
    elif i == 'v':
        ypos_r -= 1
    elif i == '>':
        xpos_r += 1
    elif i == '<':
        xpos_r -= 1
    ps_r = str(xpos_r) + ',' + str(ypos_r)
    if ps_r not in list(positions.keys()):
        positions[ps_r] = 1
    elif ps_r in list(positions.keys()):
        positions[ps_r] += 1

print len(positions)
