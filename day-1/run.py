def get_first_val_of_line(line):
    for char in line:
        if char.isnumeric():
            return int(char)

with open('input.txt') as file:
    sum = 0
    for line in file:
        tens = get_first_val_of_line(line)
        ones = get_first_val_of_line(reversed(line))
        sum += tens * 10 + ones
        
    print(sum)