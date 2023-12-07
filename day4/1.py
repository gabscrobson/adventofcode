import re

result = 0

with open('input.txt') as f:
    lines = f.read().splitlines()

for line in lines:
    numbers = re.findall(r'\d+|\|', line)
    is_have_numbers = False
    winning_numbers = set()
    card_value = 0
    
    for number in numbers[1:]:
        if number == '|':
            is_have_numbers = True
            continue
        
        if is_have_numbers:
            if number in winning_numbers:
                if card_value == 0:
                    card_value += 1
                else:
                    card_value *= 2
        else:
            winning_numbers.add(number)
    
    print(f"Card {numbers[0]}: {card_value}")
    result += card_value

print(result)
        