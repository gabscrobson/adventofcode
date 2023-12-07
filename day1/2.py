result = 0

with open('input.txt') as f:
    lines = f.readlines()

spelled_digits = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}

for line in lines:
    l, r = 0, len(line)-1

    # Left
    while l < len(line):
      if line[l].isdigit():
         l_digit = line[l]
         break

      remainings = list(spelled_digits.keys())
      curr = ''
      old_l = l
      found = False

      while remainings:
        curr += line[l]

        new_remainings = []
        for remaining in remainings:
          if curr[len(curr)-1] == remaining[len(curr)-1]:
              new_remainings.append(remaining)
        remainings = new_remainings
        
        if remainings and len(curr) == len(remainings[0]):
          l_digit = spelled_digits[curr]
          found = True
          break

        l += 1

      if found:
         break
      
      l = old_l
      l += 1

    # Right
    while r < len(line):
      if line[r].isdigit():
        r_digit = line[r]
        break

      remainings = list(spelled_digits.keys())
      curr = ''
      old_r = r
      found = False

      while remainings:
        curr += line[r]

        new_remainings = []
        for remaining in remainings:
          if curr[len(curr)-1] == remaining[-len(curr)]:
              new_remainings.append(remaining)
        remainings = new_remainings
        
        if remainings and len(curr) == len(remainings[0]):
          r_digit = spelled_digits[curr[::-1]]
          found = True
          break

        r -= 1

      if found:
        break
      
      r = old_r
      r -= 1

    print(f"({line[:-1]}) l_digit: {l_digit}, r_digit: {r_digit} => {int(l_digit + r_digit)}")
    result += int(l_digit + r_digit)

print(result)