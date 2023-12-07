result = 0

directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
not_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']
digits_map = {}

with open('input.txt') as f:
    lines = f.read().splitlines()

for i, line in enumerate(lines):
    n = ''
    positions = []

    for j, c in enumerate(line):
        if c.isdigit():
            n += c
            positions.append((i, j))
        else:
            if n != '':
                for pos in positions:
                    digits_map[pos] = int(n)
            n = ''
            positions = []

    # Check for last character
    if n != '':
        for pos in positions:
            digits_map[pos] = int(n)

print(digits_map)

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        if c == '*':
            numbers = []
            for dy, dx in directions:
                print(f"Checking {i+dy}, {j+dx}")
                if (i+dy, j+dx) in digits_map:
                    if digits_map[(i+dy, j+dx)] not in numbers:
                      print(f"Found {digits_map[(i+dy, j+dx)]}")
                      numbers.append(digits_map[(i+dy, j+dx)])
            if len(numbers) == 2:
                result += numbers[0] * numbers[1]

print(result)