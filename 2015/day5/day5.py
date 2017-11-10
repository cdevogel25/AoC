import string

#three vowels?
vowels = ['a', 'e', 'i', 'o', 'u']
#double letter?
doubles = []
for i in string.ascii_lowercase:
    doubles.append(i+i)
#no 'ab', 'cd', 'pq', 'xy'
bad_str = ['ab', 'cd', 'pq', 'xy']
nice_str = 0

f = open('./day5.txt', 'r')
s = f.readlines()
for i in s:
    nice = False
    if not any(n in i for n in bad_str):
        if any(n in i for n in doubles):
            v_count = 0
            for c in range(0,len(i)):
                if i[c] in vowels:
                    v_count += 1
                if v_count == 3:
                    nice = True
    if nice:
        print i
        nice_str += 1

print nice_str
