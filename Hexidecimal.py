def hex_to_decimal(hex_string):
    try:
        decimal_num = int(hex_string, 16)
        return decimal_num
    except ValueError:
        return "Invalid hexadecimal input"

# Example usage:
hexadecimal_input = input("Enter a hexadecimal number: ")

decimal_result = hex_to_decimal(hexadecimal_input)
if type(decimal_result) == int:
    print(f"Decimal equivalent: {decimal_result}")
else:
    print(decimal_result)
    
