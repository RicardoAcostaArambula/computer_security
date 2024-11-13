import os
def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        # lowercase letters
        if char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # digits
        elif char.isdigit():
            result += chr((ord(char) + shift - 48) % 10 + 48)
        # Leave non-alphanumeric characters unchanged
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    # decrypting with negative shift
    return caesar_cipher_encrypt(text, -shift)

if __name__ == "__main__":
    original_message = "192.168.1.10 and 192.168.1.20"
    # Key for Caesar cipher shift
    shift_key = 5  

    # Encrypt the message
    encrypted_message = caesar_cipher_encrypt(original_message, shift_key)
    print("Encrypted message:", encrypted_message)

    directory = "/home/acostaricardo463/challenges"
    file_path = os.path.join(directory, "encrypted_message.txt")

    with open(file_path, "w") as file:
        file.write(encrypted_message)
    # Decrypt the message to verify
    decrypted_message = caesar_cipher_decrypt(encrypted_message, shift_key)
<<<<<<< HEAD
<<<<<<< HEAD
    # print("Decrypted message:", decrypted_message)


=======
    print("Decrypted message:", decrypted_messag
>>>>>>> ce2167b (comments)
=======
    print("Decrypted message:", decrypted_message)


>>>>>>> b2760d6 (comments)
