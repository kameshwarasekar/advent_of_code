import hashlib

puzzle_key = "bgvyzdsv"
zeroes = "00000"
counter = 1


while 1:
    input = (puzzle_key + str(counter)).encode()
    hash = hashlib.md5(input)
    if hash.hexdigest()[:5] == zeroes:
        print(counter)
        break
    counter += 1
