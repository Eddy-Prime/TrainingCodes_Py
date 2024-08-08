import struct

def twos_complement(num, bits):
    """Convert a number to its 2's complement representation."""
    if num < 0:
        num = (1 << bits) + num
    format_string = '{:0' + str(bits) + 'b}'
    return format_string.format(num)

def float_to_ieee754(num, shorten=True):
    """Convert a float to its IEEE-754 single precision representation."""
    packed = struct.pack('!f', num)
    integer = struct.unpack('!I', packed)[0]
    binary = f'{integer:032b}'
    
    if shorten:
        sign = binary[0]
        exponent = binary[1:9]
        mantissa = binary[9:]
        mantissa = mantissa.rstrip('0')
        if mantissa == '':
            mantissa = '0'
        return f'{sign} {exponent} {mantissa}'
    else:
        return binary

def ieee754_to_float(binary):
    """Convert an IEEE-754 single precision representation to float."""
    # Remove spaces if present
    binary = binary.replace(" ", "")
    # Pad with zeros if shortened
    binary = binary.ljust(32, '0')
    integer = int(binary, 2)
    packed = struct.pack('!I', integer)
    return struct.unpack('!f', packed)[0]

def main():
    while True:
        print("\nData Representation Tools")
        print("1. 2's Complement")
        print("2. Float to IEEE-754 (Shortened)")
        print("3. Float to IEEE-754 (Full)")
        print("4. IEEE-754 to Float")
        print("5. Quit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            num = int(input("Enter an integer: "))
            bits = int(input("Enter number of bits: "))
            result = twos_complement(num, bits)
            print(f"2's complement: {result}")
        
        elif choice == '2':
            num = float(input("Enter a float: "))
            result = float_to_ieee754(num, shorten=True)
            print(f"IEEE-754 (Shortened): {result}")
        
        elif choice == '3':
            num = float(input("Enter a float: "))
            result = float_to_ieee754(num, shorten=False)
            print(f"IEEE-754 (Full): {result}")
        
        elif choice == '4':
            binary = input("Enter IEEE-754 representation: ")
            result = ieee754_to_float(binary)
            print(f"Float: {result}")
        
        elif choice == '5':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()