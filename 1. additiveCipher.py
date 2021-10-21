def encrypt(plaintext, shift):
    """
    This function encrypts the text.
    """
    ciphertext = ""

    # traversing the text and enctypting it using the key provided
    for char in plaintext:
        ciphertext += str(chr(ord(char) + shift))
  
    return ciphertext


def decrypt(ciphertext, shift):
    """
    This function encrypts the text.
    """
    plaintext = ""

    # traversing the text and decrypting it using the key provided
    for char in ciphertext:
        plaintext += chr(ord(char) - shift)

    return plaintext


def main():
    print("""
Additive cipher:
0. Exit
1. Encrypt
2. Decrypt""")

    ch = 1
    while(ch != 0):
        ch = int(input("\nEnter your choice: "))
        if(ch == 1):
            plaintext = input("\nEnter plaintext: ")
            shift = input("Enter key: ")
            while not shift.isdigit():
                shift = input("The key should be an integer, Enter again: ")

            ciphertext = encrypt(plaintext, int(shift))
            print("Encrypted text : " + ciphertext)
        
        elif(ch == 2):
            plaintext = input("\nEnter encrypted text: ")
            shift = input("Enter key: ")
            while not shift.isdigit():
                shift = input("The key should be an integer, Enter again: ")

            plaintext = decrypt(ciphertext, int(shift))
            print(("Decrypted text : " + plaintext))

        
if __name__ == "__main__":
    main()
