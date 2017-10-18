def surface_area(sides):
    sides = sides.rstrip()
    side_arr = sides.split('x')
    l = int(side_arr[0])
    w = int(side_arr[1])
    h = int(side_arr[2])
    sa = [(l*w), (w*h), (h*l)]
    extra = min(sa)
    return 2*sa[0] + 2*sa[1] + 2*sa[2] + extra

f = open('./day2.txt', 'r')
s = f.readlines()
sa = 0;
for i in s:
    sa += surface_area(i)

print sa
