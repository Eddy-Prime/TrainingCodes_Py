def binary_to_decimal(binary_str):
    try:
        decimal_num = int(binary_str, 2)
        return decimal_num
    except ValueError:
        return "Invalid binary input"

# Input a binary number as a string
binary_input = input("Enter a binary number: ")

# Call the function to convert to decimal and print the result
decimal_result = binary_to_decimal(binary_input)
print("Decimal equivalent:", decimal_result)

