#Encrypt the text using Caesar cipher with the given shift.
def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted = ord(char) + shift_amount
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

#Decrypt the text using Caesar cipher with the given shift.
def decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_amount = shift % 26
            shifted = ord(char) - shift_amount
            if char.islower():
                if shifted < ord('a'):
                    shifted += 26
                decrypted_text += chr(shifted)
            elif char.isupper():
                if shifted < ord('A'):
                    shifted += 26
                decrypted_text += chr(shifted)
        else:
            decrypted_text += char
    return decrypted_text

def main():
    print("Caesar Cipher Program")
    choice = input("Would you like to (E)ncrypt or (D)ecrypt a message? ").strip().upper()
    
    if choice not in ['E', 'D']:
        print("Invalid choice. Please select 'E' to encrypt or 'D' to decrypt.")
        return

    message = input("Enter your message: ").strip()
    try:
        shift = int(input("Enter the shift value: ").strip())
    except ValueError:
        print("Invalid shift value. Please enter a number.")
        return
    
    if choice == 'E':
        result = encrypt(message, shift)
        print(f"Encrypted message: {result}")
    elif choice == 'D':
        result = decrypt(message, shift)
        print(f"Decrypted message: {result}")

if __name__ == "__main__":
    main()
