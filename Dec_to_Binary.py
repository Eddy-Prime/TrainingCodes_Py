def decimal_to_binary(decimal_str, bit_length=16):
    try:
        decimal_num = int(decimal_str, 10)
        binary_num = bin(decimal_num)[2:]  # Convert to binary and remove the '0b' prefix
        # Ensure the binary string is exactly 'bit_length' characters long by adding leading zeros if needed
        
        return binary_num
    except ValueError:
        return "Invalid Decimal input"

# Input a decimal number as a string
Decimal_input = input("Enter a Decimal number: ")

# Call the function to convert to a 16-bit binary representation and print the result
binary_result = decimal_to_binary(Decimal_input)
print("16-bit Binary equivalent:", binary_result)
