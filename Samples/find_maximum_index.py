def find_maximum_index(numbers):
    # Find the index of the maximum value in the list
    max_index = numbers.index(max(numbers))
    return max_index

def move_maximum_to_end(numbers):
    # Find the index of the maximum value
    max_index = find_maximum_index(numbers)

    # Move the maximum value to the end of the list
    max_value = numbers.pop(max_index)
    numbers.append(max_value)

# Example usage:
numbers = [3, 8, 2, 5, 10, 7]

# Using find_maximum_index
max_index = find_maximum_index(numbers)
print("Index of maximum value:", max_index)

# Using move_maximum_to_end
move_maximum_to_end(numbers)
print("List after moving maximum to the end:", numbers)


#/////Explanation/////


#find_maximum_index function:


#Uses the max function to find the maximum value in the list.
#Uses the index method to find the index of the maximum value.
#Returns the index.
#move_maximum_to_end function:

#Calls find_maximum_index to get the index of the maximum value.
#Uses pop to remove the maximum value from its current position.
#Uses append to add the maximum value to the end of the list.
