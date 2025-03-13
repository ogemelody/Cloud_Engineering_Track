def encrypt_char(char, key):
    """

    :param char:  input the alphabet
    :param key: The shift amount for the Caesar cipher.(the position of alphabet to be retrieved)
    :return: new alphabet (The encrypted character).
    """
    position = ord(char) - ord('a')
    new_position = (position + key) % 26

    new_char = chr(new_position + ord('a'))
    return new_char

def encrypt_caesar(text, key):
    """Encrypts a full text string using the Caesar cipher."""
    encrypted_text = ""  # Start with an empty string
    for char in text:  # Loop through each character
        encrypted_text += encrypt_char(char, key)  # Encrypt and append
    return encrypted_text  # Return the encrypted result

def decrypt_char(char, key):
    """Decrypts a single character using the Caesar cipher."""
    position = ord(char) - ord('a')  # Get 0-based index of char
    new_position = (position - key) % 26  # Shift backwards with wrap-around
    return chr(new_position + ord('a'))

def decrypt_caesar(ciphertext, key):
    """Decrypts a full ciphertext string using the Caesar cipher."""
    decrypted_text = ""  # Start with an empty string
    for char in ciphertext:  # Loop through each character
        decrypted_text += decrypt_char(char, key)  # Decrypt and append
    return decrypted_text  # Return the decrypted result


print(encrypt_char('a', -2))
print(encrypt_caesar('learning', 3))
print(decrypt_caesar('bcd', 4))  # Output: 'xyz'