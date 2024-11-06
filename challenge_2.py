import os
def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        # handling lowercase letters
        if char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # handling numbers
        elif char.isdigit():
            result += chr((ord(char) + shift - 48) % 10 + 48)
        # anything else
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    # decrypting with negative shift 
    return caesar_cipher_encrypt(text, -shift)

if __name__ == "__main__":
    original_message = "192.168.1.10 and 192.168.1.20"
    # Key for Caesar cipher shift which is the same key from previous challenge 
    shift_key = 5  

    # Encrypted message
    encrypted_message = caesar_cipher_encrypt(original_message, shift_key)
    print("Encrypted message:", encrypted_message)
    # path may need adjustments based on user
    directory = "/home/acostaricardo463/challenges"
    file_path = os.path.join(directory, "encrypted_message.txt")

    with open(file_path, "w") as file:
        file.write(encrypted_message)
    # Decrypted message for set up reference
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift_key)
    print("Decrypted message:", decrypted_message)


