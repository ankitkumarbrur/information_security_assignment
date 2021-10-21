from collections import defaultdict

def frequencyAttack(S):
    # calculating the length of string & converting the string to uppercase to avoid any snag in frequency attack
    N, S = (len(S), S.upper())

    # List to store the top plain texts
    plaintext = []              

    # storing the english letters in their decreasing order of frequency
    english_letter_frequency = "ETAOINSHRDLCUMWFGYPBVKJXQZ"

    # dictionary to store frequency of the letters in cipher text  
    frequency = defaultdict(int)    

    # calculating the frequency of the letters in cipher text
    for c in S: frequency[c] += 1

    # In python 3.7+ dictionary preserves the insertion order (NOTE: program may not work as expected if we use dictionary and run on python version < 3.7)
    # sorted_frequency = dict(sorted(fr.items(), key = lambda i: i[1], reverse=True))
    
    # Sorting frequency and storing it in a tuple
    sorted_frequency = tuple(sorted(frequency.items(), key = lambda i: i[1], reverse=True))


    for i in range(26):
        # calculating the key
        key = (26 + ord(sorted_frequency[0][0]) - ord(english_letter_frequency[i])) % 26
        txt = ""

        # time complexity : O(26 * N)
        for j in range(len(S)):
            # traversing on string and decoding it
            if(S[j] >= 'A' and S[j] <= 'Z'):
                txt += chr(65 + (ord(S[j]) - 65 + key) % 26)
            else: 
                txt += S[j]

        plaintext.append(txt)

    return plaintext

S = input("Enter encoded string: ")
pt = int(input("Enter how many plain texts you want (max: 26): "))

# calling the function to get plaintexts
plaintext = frequencyAttack(S)

print("\n\nDECODED PLAIN TEXTS:\n")
# printing the plaintexts
for i in range(pt % 26):
    print( i + 1, end = ": ")
    print( plaintext[i], end = "\n\n")