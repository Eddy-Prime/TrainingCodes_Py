def binary_addition(bin1, bin2, bit_length=16):
    try:
        result = bin(int(bin1, 2) + int(bin2, 2))[2:]
        # Ensure the result is exactly 'bit_length' characters long by adding leading zeros if needed
        result = result.zfill(bit_length)
        return result
    except ValueError:
        return "Invalid binary input"

# Input two binary numbers as strings
binary1 = input("Enter the first binary number: ")
binary2 = input("Enter the second binary number: ")

# Choose the operation
operation = input("Choose operation (+, -, *, /): ")

if operation == '+':
    result = binary_addition(binary1, binary2, 16)
    print(f"Result: {result}")
else:
    print("Invalid operation selected.")
