numbers = [20, 36, 12, 24, 20, 48, 74, 353, 23, 98]
largest_number = numbers[0]
for number in numbers:
    if number > largest_number:
        largest_number = number
print(largest_number)
