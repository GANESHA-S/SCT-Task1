def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Welcome to the Caesar Cipher Program!")
    while True:
        choice = input("Press (E)Encrypt, (D)Decrypt, or (Q)Quit? ").strip().lower()
        if choice == 'e':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value (integer): "))
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == 'd':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value (integer): "))
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")
        elif choice == 'q':
            print("Bye!")
            break
        else:
            print("Invalid choice.Try again.")

if __name__ == "__main__":
    main()
