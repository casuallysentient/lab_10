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
    pass


def main():
    """
    Just some sample behavior. Feel free to tru your own!
    """

    binary_list = [1, 0, 0, 1, 1, 1, 0, 1]  # be mindful about not changing this list in your functions

    # Problem 1.1
    print(binary_to_decimal(binary_list))

    # Problem 1.2
    # print(binary_to_hex(binary_list))  # uncomment to test

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
