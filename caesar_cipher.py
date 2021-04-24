def decode_caesar(encoded_message, key):
    """
    Using the value contained in key, decrypts all alphabetic characters in encoded_message. Includes all non-alpha
    characters in decoded-message NOT decrypted.

    :param encoded_message: String encrypted by the Caesar cipher.
    :param key: Integer used for decryption.
    :return: Decrypted string.
    """
    alphabet = {
            'a': 1,
            'b': 2,
            'c': 3,
            'd': 4,
            'e': 5,
            'f': 6,
            'g': 7,
            'h': 8,
            'i': 9,
            'j': 10,
            'k': 11,
            'l': 12,
            'm': 13,
            'n': 14,
            'o': 15,
            'p': 16,
            'q': 17,
            'r': 18,
            's': 19,
            't': 20,
            'u': 21,
            'v': 22,
            'w': 23,
            'x': 24,
            'y': 25,
            'z': 26,

            'A': 101,
            'B': 102,
            'C': 103,
            'D': 104,
            'E': 105,
            'F': 106,
            'G': 107,
            'H': 108,
            'I': 109,
            'J': 110,
            'K': 111,
            'L': 112,
            'M': 113,
            'N': 114,
            'O': 115,
            'P': 116,
            'Q': 117,
            'R': 118,
            'S': 119,
            'T': 120,
            'U': 121,
            'V': 122,
            'W': 123,
            'X': 124,
            'Y': 125,
            'Z': 126
        }
    reversed_alphabet = {value: key for (key, value) in alphabet.items()}

    decoded_message = ""
    for char in encoded_message:
        if char.isalpha():
            code = alphabet[char] - key
            if 26 < code < 101 or code < 1:
                code += 26
            decoded_message += reversed_alphabet[code]
        else:
            decoded_message += char
    return decoded_message


def main():
    """
    Just some sample behavior.
    """
    decryption_key = 3

    try:
        file = open("calling_america_lyrics.txt", 'r')
    except FileNotFoundError:
        print("ERROR: File not found!")
    else:
        for line in file:
            line = line.strip()
            decryption = decode_caesar(line, decryption_key)
            print(decryption)

        file.close()

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
