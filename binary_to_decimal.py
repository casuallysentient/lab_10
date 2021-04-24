def binary_to_decimal(binary_list):
    """
    Converts a binary number, represented by the values inside binary_list, to its decimal equivalent.

    :param binary_list: A list of ones and zeroes.
    :return: An integer.
    """
    decimal = 0
    index = 0
    for character in reversed(binary_list):
        decimal += (character * (2 ** index))
        index += 1
    return decimal


def binary_to_hex(binary_list):
    """
    Converts a binary number, represented by the values inside binary_list, to its hexadecimal equivalent.

    :param binary_list: A list of ones and zeroes of size 4n.
    :return: A string representing a hex number.
    """
    hex_converter = {"0000": 0, "0001": 1, "0010": 2, "0011": 3, "0100": 4, "0101": 5, "0110": 6, "0111": 7, "1000": 8, "1001": 9, "1010": "a", "1011": "b", "1100": "c", "1101": "d", "1110": "e", "1111": "f"}
    while len(binary_list) % 4 != 0:
        binary_list.insert(0, 0)
    digits_checked = 0
    segment = ""
    translation = ""
    for digit in binary_list:
        segment += str(digit)
        digits_checked += 1
        if digits_checked == 4:
            segment = hex_converter[segment]
            translation += str(segment)
            digits_checked = 0
            segment = ""
    return translation


def main():
    """
    Just some sample behavior. Feel free to tru your own!
    """

    binary_list = [1, 1, 0, 0, 1, 1, 1, 0, 1]  # be mindful about not changing this list in your functions
    # Problem 1.1
    print(binary_to_decimal(binary_list))

    # Problem 1.2
    print(binary_to_hex(binary_list))  # uncomment to test

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
