def binary_addition(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:]

def binary_subtraction(bin1, bin2):
    return bin(int(bin1, 2) - int(bin2, 2))[2:]

def binary_multiplication(bin1, bin2):
    return bin(int(bin1, 2) * int(bin2, 2))[2:]

def binary_division(bin1, bin2):
    try:
        quotient = int(bin1, 2) // int(bin2, 2)
        remainder = int(bin1, 2) % int(bin2, 2)
        return bin(quotient)[2:], bin(remainder)[2:]
    except ZeroDivisionError:
        return "Cannot divide by zero."

# Input two binary numbers as strings
binary1 = input("Enter the first binary number: ")
binary2 = input("Enter the second binary number: ")

# Choose the operation
operation = input("Choose operation (+, -, *, /): ")

if operation == '+':
    result = binary_addition(binary1, binary2)
elif operation == '-':
    result = binary_subtraction(binary1, binary2)
elif operation == '*':
    result = binary_multiplication(binary1, binary2)
elif operation == '/':
    quotient, remainder = binary_division(binary1, binary2)
    result = f"Quotient: {quotient}, Remainder: {remainder}"
else:
    result = "Invalid operation."

print(f"Result: {result}")
