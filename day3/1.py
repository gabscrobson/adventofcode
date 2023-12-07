result = 0

directions = [[-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1]]
not_symbols = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.']

with open('input.txt') as f:
    lines = f.read().splitlines()

for i, line in enumerate(lines):
    n = ''
    have_symbol = False

    for j, c in enumerate(line):
        if c.isdigit():
            n += c
            if not have_symbol:
              for dy, dx in directions:
                  try:
                    if lines[i+dy][j+dx] not in not_symbols:
                        have_symbol = True
                        break
                  except:
                    pass
        else:
            if have_symbol:
                old_result = result
                result += int(n)
            n = ''
            have_symbol = False

    # Check for last character
    if have_symbol:
        old_result = result
        result += int(n)

print(result)