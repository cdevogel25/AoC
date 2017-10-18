def ribbon(sides):
    sides = sides.rstrip()
    side_arr = sides.split('x')
    side_arr = map(int, side_arr)
    side_arr = sorted(side_arr)
    ribbon_len = (2*side_arr[0] + 2*side_arr[1])
    ribbon_len += (side_arr[0]*side_arr[1]*side_arr[2])
    return ribbon_len

f = open('./day2.txt', 'r')
s = f.readlines()
ribbon_len = 0
for i in s:
    ribbon_len += ribbon(i)

print ribbon_len
