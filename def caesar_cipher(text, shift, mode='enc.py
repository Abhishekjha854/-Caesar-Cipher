def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    
    # Adjust the shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Keep any non-alphabet characters as they are
            result += char
    
    return result

# Get user input
text = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").lower()

# Encrypt or decrypt based on user choice
if mode in ['encrypt', 'decrypt']:
    result = caesar_cipher(text, shift, mode)
    print(f"The {mode}ed text is: {result}")
else:
    print("Invalid mode selected.")
