# pip install numpy
# pip install egcd

import numpy as np
from egcd import egcd

alphabet = "abcdefghijklmnopqrstuvwxyz "

letter_to_index = dict(zip(alphabet, range(len(alphabet))))
index_to_letter = dict(zip(range(len(alphabet)), alphabet))

def matrixModulusInverse(matrix):

    # Finding determinant
    det = int(np.round(np.linalg.det(matrix)))

    # Regularising determinant
    det_inv = egcd(det, 26)[1] % 26 

    # regularised determinant * (det * inverted_matrix ) % 26
    return ( det_inv * np.round(det * np.linalg.inv(matrix)).astype(int) % 26)


def encrypt(plaintext, secret_key):
    ln = len(plaintext)
    encrypted = ""
    # vector -> letters to numbers converted
    vector = [letter_to_index[i] for i in plaintext]

    # mapping vector to secret key matrix dimensions
    mapped_plaintext = [ vector[i: i + int(secret_key.shape[0])] for i in range(0, len(vector), int(secret_key.shape[0]))]

    # encryping the text 
    for numbered_plaintext in mapped_plaintext:
        numbered_plaintext = np.transpose(np.asarray(numbered_plaintext))[:, np.newaxis]

        while numbered_plaintext.shape[0] != secret_key.shape[0]:
            numbered_plaintext = np.append(numbered_plaintext, 27)[:, np.newaxis]

        numbers = np.dot(secret_key, numbered_plaintext) % 26

        # Map back to get encrypted text
        for i in range(numbers.shape[0]):
            number = int(numbers[i, 0])
            encrypted += index_to_letter[number]

    return encrypted[:ln]


def decrypt(cipher, K_inverse):
    ln = (len(cipher) % K_inverse.shape[0])
    cipher += "b"*ln
    decrypted = ""
    # vector -> letters to numbers converted
    vector = [letter_to_index[i] for i in cipher]

    # mapping vector to secret key matrix dimensions
    mapped_cipher = [ vector[i: i + int(K_inverse.shape[0])] for i in range(0, len(vector), int(K_inverse.shape[0])) ]

    for numbered_ciphertext in mapped_cipher:
        numbered_ciphertext = np.transpose(np.asarray(numbered_ciphertext))[:, np.newaxis]

        numbers = np.dot(K_inverse, numbered_ciphertext) % 26

        for i in range(numbers.shape[0]):
            number = int(numbers[i, 0])
            decrypted += index_to_letter[number]

    return decrypted[:len(cipher)-ln]

def main():
    #spaces are not supported
    plaintext = 'informationsecurity'

    # Secret Key Matrix
    secret_key = np.matrix([[3, 3], [2, 5]])

    # Secret Key Matrix Inverse
    K_inverse = matrixModulusInverse(secret_key)

    encrypted_text = encrypt(plaintext, secret_key)
    decrypted_text = decrypt(encrypted_text, K_inverse)

    
    print("Original text: " + plaintext)
    print("Encrypted text: " + encrypted_text)
    print("Decrypted text: " + decrypted_text)


if __name__ == "__main__":
    main()