import re

result = 0

with open('input.txt') as f:
    lines = f.read().splitlines()

# Amount of copies of each card
copies = {}

for line in lines:
    numbers = re.findall(r'\d+|\|', line)
    card_number = int(numbers[0])
    is_have_numbers = False
    winning_numbers = set()
    matching_numbers = 0

    # Add card to copies if not exists
    if card_number not in copies:
      copies[card_number] = 1
    
    for number in numbers[1:]:
        if number == '|':
            is_have_numbers = True
            continue
        
        if is_have_numbers:
            if number in winning_numbers:
                matching_numbers += 1
        else:
            winning_numbers.add(number)
    
    print(f"Card {card_number}: {matching_numbers} | copies: {copies[card_number]}")

    # Increment copies of cards that will be copied
    for i in range(card_number+1, card_number + matching_numbers + 1):
        if i not in copies:
            copies[i] = 1
        copies[i] += 1*copies[card_number]
        print(f"Added {1*copies[card_number]} copies of {i}")

    print("--------------------")

print(sum(copies.values()))
        