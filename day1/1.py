result = 0

with open('input.txt') as f:
    lines = f.readlines()

for line in lines:
    
    l, r = 0, len(line)-1

    while not line[l].isdigit():
        l += 1

    while not line[r].isdigit():
        r -= 1

    result += int(line[l] + line[r])

print(result)