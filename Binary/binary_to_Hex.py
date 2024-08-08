def binary_to_hex(binary_string):
    # Remove any spaces from the binary string
    binary_string = binary_string.replace(" ", "")
    
    # Ensure the input is a valid binary number
    if not all(bit in '01' for bit in binary_string):
        return "Invalid binary input. Please use only 0s and 1s."
    
    # Pad the binary string with zeros if necessary to make its length a multiple of 4
    while len(binary_string) % 4 != 0:
        binary_string = '0' + binary_string
    
    # Dictionary to map groups of 4 binary digits to hexadecimal
    bin_to_hex = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    
    hex_result = ''
    for i in range(0, len(binary_string), 4):
        chunk = binary_string[i:i+4]
        hex_result += bin_to_hex[chunk]
    
    return hex_result

# Main loop
while True:
    binary_input = input("Enter a binary number (or 'q' to quit): ")
    
    if binary_input.lower() == 'q':
        print("Thank you for using the converter. Goodbye!")
        break
    
    hex_output = binary_to_hex(binary_input)
    print(f"Binary: {binary_input}")
    print(f"Hexadecimal: {hex_output}")
    print()  # Add a blank line for readability