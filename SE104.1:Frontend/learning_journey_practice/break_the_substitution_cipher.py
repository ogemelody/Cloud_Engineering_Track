import string


# Step 1: Load the encrypted book from a file
def load_encrypted_book(file_path):
    with open(file_path, 'r') as file:
        encrypted_text = file.read()
    return encrypted_text


# Step 2: Decrypt the text using the provided mapping
def decrypt_text(encrypted_text, mapping):
    decrypted_text = []
    for char in encrypted_text:
        if char.isalpha():
            # Convert to lowercase and find the corresponding letter in the mapping
            mapped_char = mapping.get(char.lower(), char.lower())  # Use .get() to handle missing keys
            # If the character was uppercase, convert it back to uppercase
            if char.isupper():
                decrypted_text.append(mapped_char.upper())
            else:
                decrypted_text.append(mapped_char)
        else:
            # Non-alphabetic characters remain unchanged
            decrypted_text.append(char)

    return ''.join(decrypted_text)


# Main function to execute the decryption process
def main():
    file_path = 'encrypted_book.txt'  # Replace with your actual file path
    encrypted_text = load_encrypted_book(file_path)

    # Mapping derived from frequency analysis
    cipher = {
        'a': 's', 'b': 'b', 'c': 'd', 'd': 'f', 'e': 'k', 'f': 'h', 'g': 'x', 'h': 'c', 'i': 'e',
        'j': 'y', 'k': 't', 'l': 'v', 'm': 'w', 'n': 'l', 'o': 'u', 'p': 'q', 'q': 'p', 'r': 'r',
        's': 'j', 't': 'i', 'u': 'o', 'v': 'm', 'w': 'n', 'x': 'a', 'y': 'z', 'z': 'g'
    }

    # Step 3: Decrypt the text
    decrypted_text = decrypt_text(encrypted_text, cipher)
    print(decrypted_text [493:782])
    print(decrypted_text[784: 1009])
    # Optionally, write the decrypted text to a new file
    with open('decrypted_book.txt', 'w') as file:
        file.write(decrypted_text)

    print("Decryption completed. Check 'decrypted_book.txt' for the result.")


if __name__ == "__main__":
    main()
