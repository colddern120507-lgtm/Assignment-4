def sum_numbers(number_list):
    total = 0
    for num in number_list:
        total += num
    return total


# Main program
numbers = [1, 2, 3, 4, 5]

result = sum_numbers(numbers)

print("The sum is:", result)