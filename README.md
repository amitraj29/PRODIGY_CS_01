---

# Caesar Cipher Tool

This Python script allows you to encrypt and decrypt messages using the Caesar Cipher technique. The Caesar Cipher is a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet.

## Features
- Encrypt messages
- Decrypt messages
- Handles both uppercase and lowercase letters
- Retains non-alphabetic characters unchanged

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/amitraj29/PRODIGY_CS_01.git
   cd MACChangerTool
   ```

2. **Run the script:**
   ```bash
   python caesar_cipher.py
   ```

3. **Follow the prompts:**
   - Enter your message
   - Enter the key (an integer for the shift value)
   - Specify whether you want to 'encrypt' or 'decrypt' the message

## Example

### Encrypting a Message

```
Enter your message: Hello World
Enter the key (integer): 3
Would you like to encrypt or decrypt the message? (enter 'encrypt' or 'decrypt'): encrypt
The encrypted message is: Khoor Zruog
```

### Decrypting a Message

```
Enter your message: Khoor Zruog
Enter the key (integer): 3
Would you like to encrypt or decrypt the message? (enter 'encrypt' or 'decrypt'): decrypt
The decrypted message is: Hello World
```

## Code Explanation

### `caesar_cipher` Function

This function takes three parameters:
- `message`: The input text to be encrypted or decrypted.
- `key`: The number of positions each letter in the message is shifted.
- `mode`: A string indicating whether to 'encrypt' or 'decrypt' the message.

The function processes each character in the message, shifts alphabetic characters by the specified key, and leaves non-alphabetic characters unchanged.

### `main` Function

This function handles user interaction:
- Prompts the user for input
- Validates the mode (either 'encrypt' or 'decrypt')
- Calls the `caesar_cipher` function with the provided inputs
- Prints the result

## Contributing

Feel free to fork this repository, make improvements, and submit pull requests. Contributions are welcome!

## Contact

For any questions or suggestions, please open an issue or contact me at amitrajkarmakar29@gmail.com.

---
