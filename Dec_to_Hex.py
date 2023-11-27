def decimal_to_hex(decimal_num):
    try:
        hex_string = hex(decimal_num)
        return hex_string[2:]  # Remove the "0x" prefix from the hexadecimal string
    except ValueError:
        return "Invalid decimal input"

# Example usage:
decimal_input = input("Enter a decimal number: ")

try:
    decimal_input = int(decimal_input)
    hexadecimal_result = decimal_to_hex(decimal_input)
    print(f"Hexadecimal equivalent: {hexadecimal_result}")
except ValueError:
    print("Invalid input. Please enter a valid decimal number.")
