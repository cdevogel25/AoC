import hashlib
input_s = 'bgvyzdsv'
found_hash = False
i = 0
while not found_hash:
    i += 1
    hash_s = input_s + str(i)
    m = hashlib.md5(hash_s)
    if str(m.hexdigest())[0:6] == '000000':
        found_hash = True

print i
