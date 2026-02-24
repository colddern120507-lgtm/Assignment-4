def remove_odd_numbers(number_list):
    new_list = []

    for num in number_list:
        if num % 2 == 0:
            new_list.append(num)

    return new_list


# Main program
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

filtered_numbers = remove_odd_numbers(numbers)

print("Original list:", numbers)
print("List without odd numbers:", filtered_numbers)