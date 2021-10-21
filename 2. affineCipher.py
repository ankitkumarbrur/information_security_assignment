def modInverse(a, m):
    # the function to find mod inverse
    for x in range(1, m):
        if ((a % m) * (x % m)) % m == 1:
            return x
    return -1


def affine_encrypt(plaintext, key):
    # the function to encrypt the data using affine cipher
    ciphertext = ""

    for i in plaintext:
        if i == " " or i.isdigit():
            ciphertext += i
        else:
            if i.isupper():
                ciphertext += chr(((key[0] * (ord(i) - ord('A')) + key[1]) % 26) + ord('A'))
            else:
                ciphertext += chr(((key[0] * (ord(i) - ord('a')) + key[1]) % 26) + ord('a'))

    return ciphertext


def affine_decrypt(ciphertext, key):
    # the function to decrypt the data using affine cipher
    plaintext = ""

    for i in ciphertext:
        if i == " " or i.isdigit():
            plaintext += i
        else:
            if i.isupper():
                plaintext += chr(((modInverse(key[0], 26) * (ord(i) - ord('A') - key[1])) % 26) + ord('A'))
            else:
                plaintext += chr(((modInverse(key[0], 26) * (ord(i) - ord('a') - key[1])) % 26) + ord('a'))
                
    return plaintext


def main():
    # driver function
    try:
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

                # Enter key 1
                key1 = input("Enter key index 0 (a), say 17: ")
                while not key1.isdigit():
                    key1 = input("The key index 0 should be an integer, Enter again: ")

                # Enter key 2
                key2 = input("Enter key index 1 (b = coprime(a)), say 20: ")
                while not key2.isdigit():
                    key2 = input("The key index 1 should be an integer, Enter again: ")

                key = (int(key1), int(key2))

                ciphertext = affine_encrypt(plaintext, key)
                print("Encrypted text : " + ciphertext)

            
            elif(ch == 2):
                plaintext = input("\nEnter encrypted text: ")

                # Enter key 1
                key1 = input("Enter key index 0 (a), say 17: ")
                while not key1.isdigit():
                    key1 = input("The key index 0 should be an integer, Enter again: ")

                # Enter key 2
                key2 = input("Enter key index 1 (b = coprime(a)), say 20: ")
                while not key2.isdigit():
                    key2 = input("The key index 1 should be an integer, Enter again: ")

                key = (int(key1), int(key2))

                # Decrypting
                plaintext = affine_decrypt(ciphertext, key)
                print("Decrypted text : " + plaintext)

    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()


