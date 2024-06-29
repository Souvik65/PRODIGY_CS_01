def encrypt_caesar_cipher(text, shift):
    result = ""
    
    for char in text:
        if char.isupper():
            result += chr((ord(char) - 65 + shift) % 26 + 65) #ord(char) for converting into ascii
        elif char.islower():
            result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            # for space, punctuation
            result += char
            
    return result
shift=5

def decrypt_caesar_cipher(text, shift):
    return encrypt_caesar_cipher(text, -shift)


def encrypt_the_text():
    plain_text = input("\nEnter the plain text for Encryption or Decryption : ")
    encrypted_text = encrypt_caesar_cipher(plain_text, shift)
    print("\nEncrypted text:  ", encrypted_text)

def decrypt_the_text():
    encrypted_text = input("Enter the encrypted text: ")

    decrypted_text = decrypt_caesar_cipher(encrypted_text, shift)
    print("\nDecrypted text: ", decrypted_text)

def all_input():
    while True:
        option = input('''\nChoose option
            1 for Encrypt
            2 for Decrypt
            3 for Exit \n ''')
        if option == "1":
            encrypt_the_text()
        elif option == "2":
            decrypt_the_text()
        elif option =='3':
            break
        else:
            print("Invalid option. Please enter 1 or 2.")

all_input()
