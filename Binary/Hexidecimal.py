def hex_to_binary(hex_string, bits=16):
    """
    Convert a hexadecimal string to a binary string of specified bit length.
    
    Args:
    hex_string (str): A string representing a hexadecimal number.
    bits (int): The desired bit length (16 or 48).
    
    Returns:
    str: A string representing the binary equivalent.
    """
    try:
        # Remove spaces and convert to lowercase
        hex_string = hex_string.replace(" ", "").lower()
        
        # Convert hex to integer
        integer_value = int(hex_string, 16)
        
        # Convert integer to binary and ensure it's the specified bit length
        binary_string = format(integer_value, f'0{bits}b')
        
        # If the number is too large for the specified bits, truncate it
        if len(binary_string) > bits:
            binary_string = binary_string[-bits:]
        
        return binary_string
    except ValueError:
        return "Invalid hexadecimal input"

def format_binary(binary_string, group_size=4):
    """Format the binary string into groups for readability."""
    return ' '.join(binary_string[i:i+group_size] for i in range(0, len(binary_string), group_size))

def main():
    while True:
        hex_input = input("Enter a hexadecimal number or sequence (or 'q' to quit): ")
        
        if hex_input.lower() == 'q':
            print("Goodbye!")
            break
        
        bits = int(input("Enter desired bit length (16 or 48): "))
        if bits not in [16, 48]:
            print("Invalid bit length. Please enter 16 or 48.")
            continue
        
        binary_result = hex_to_binary(hex_input, bits)
        formatted_result = format_binary(binary_result)
        print(f"{bits}-bit Binary: {formatted_result}")

if __name__ == "__main__":
    main()