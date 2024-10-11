# Task 01 - Caesar Cipher Implementation
This repository contains the Python code for implementing the Caesar Cipher as part of my internship at Prodigy InfoTech.

## Instructions:
- The program encrypts and decrypts messages using a shift value provided by the user.
- To run the code, execute `task1.py` and follow the prompts.

# Function to encrypt the message using Caesar Cipher
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            shift_base = 65 if char.isupper() else 97  # Uppercase letters start at 65 in ASCII, lowercase at 97
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char  # Keep other characters (like space, punctuation) unchanged
    return encrypted_text

# Function to decrypt the message using Caesar Cipher
def decrypt(text, shift):
    return encrypt(text, -shift)

# Main function to get user input and perform encryption or decryption
def caesar_cipher():
    print("Welcome to Caesar Cipher Program")
    choice = input("Type 'e' to encrypt or 'd' to decrypt: ").lower()

    if choice not in ['e', 'd']:
        print("Invalid choice!")
        return

    message = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))
    
    if choice == 'e':
        print("Encrypted message: ", encrypt(message, shift))
    else:
        print("Decrypted message: ", decrypt(message, shift))

# Run the Caesar Cipher program
if __name__ == "__main__":
    caesar_cipher()
