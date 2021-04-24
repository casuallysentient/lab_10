from super_secrect_module import corrupter


def is_impostor(information, corrupter_function):
    """
    Returns True if function corrupter creates a deep copy of information, otherwise it returns False.

    :param information: A dictionary of a band's information.
    :param corrupter_function: A function that returns either a deep or shallow copy of the object passed onto it.
    :return: True or False
    """
    copy = corrupter_function(information)
    copy["Members"]["Guitarist"] = "your mom"
    if copy["Members"]["Guitarist"] == information["Members"]["Guitarist"]:
        return False
    return True


def main():
    """
    Just some sample behavior. Feel free to try your own!
    """
    sample_band = {
        "Band Name": "Silk Sonic",
        "Members": {
            "Guitarist": "D'Mile",
            "Bass Player": "Christopher Brody Brown",
            "Drummer": "Andreson .Paak",
            "Singer": "Bruno Marks"
        },
        "Albums": ["Leave the Door Open - Single", "An Evening with Silk Sonic"]
    }

    number_of_tests = 10  # let's test this a few times
    for test_number in range(number_of_tests):
        # the line below is just the one-liner version of the code in the README.
        print("Test #{}: is_impostor() returned a {} copy!".format(test_number + 1,
                                                                   "deep" if is_impostor(sample_band, corrupter) else
                                                                   "shallow"))

# DO NOT WRITE CODE BELOW THIS LINE


if __name__ == '__main__':
    main()
