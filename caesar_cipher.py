def decode_caesar(encoded_message, key):
    """
    Using the value contained in key, decrypts all alphabetic characters in encoded_message. Includes all non-alpha
    characters in decoded-message NOT decrypted.

    :param encoded_message: String encrypted by the Caesar cipher.
    :param key: Integer used for decryption.
    :return: Decrypted string.
    """
    pass


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
