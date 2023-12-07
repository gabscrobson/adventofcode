import re

result = 0

limit = {
    'r': 12,
    'g': 13,
    'b': 14
}

with open('input.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    maximum = {
        'r': 0,
        'g': 0,
        'b': 0
    }

    numbers = re.findall(r'\d+', line)
    colors = re.findall(r'(red|green|blue)', line)

    for i, n in enumerate(numbers[1:]):
        maximum[colors[i][0]] = max(int(n), maximum[colors[i][0]])

    if maximum['r'] <= limit['r'] and maximum['g'] <= limit['g'] and maximum['b'] <= limit['b']:
        result += int(numbers[0])

print(result)
        

