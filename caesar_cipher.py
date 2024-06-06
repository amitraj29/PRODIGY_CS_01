def caesar_cipher(message, key, mode):
    result = ""
    
    # Determine the operation: 1 for encryption, -1 for decryption
    operation = 1 if mode == 'encrypt' else -1
    
    # Adjust key based on operation
    key *= operation
    
    # Iterate over each character in the message
    for char in message:
        if char.isalpha():
            # Determine the ASCII offset based on whether the character is upper or lower case
            ascii_offset = 65 if char.isupper() else 97
            # Perform the shift operation and wrap around the alphabet using modulo
            new_char = chr((ord(char) - ascii_offset + key) % 26 + ascii_offset)
            result += new_char
        else:
            # Keep non-alphabet characters unchanged
            result += char
            
    return result

def main():
    # Get message, key, and operation from user
    message = input("Enter your message: ")
    key = int(input("Enter the key (integer): "))
    mode = input("Would you like to encrypt or decrypt the message? (enter 'encrypt' or 'decrypt'): ").lower()
    
    # Validate the mode input
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode! Please enter 'encrypt' or 'decrypt'.")
        return
    
    # Perform the operation
    result = caesar_cipher(message, key, mode)
    print(f"The {mode}ed message is: {result}")

if __name__ == "__main__":
    main()