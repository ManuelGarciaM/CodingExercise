from __future__ import print_function  # This line is so that the following code will run in both python 2 and 3


def get_alphbet_dict():
    """
    Gets lookup values for ordering of each letter.
    I generate this using ascii values so that I know it'll be more accurate than typing it out
    :return: dict, {'a':1, 'b':2, ...}
    """
    alphabet_dict = {}

    # Get the ascii value of the first and last letter
    first_letter_value = ord('a')
    last_letter_value = ord('z')

    for ascii_value in range(first_letter_value, last_letter_value + 1):
        # Convert value to chr, and store the number starting from 1 for a
        letter = chr(ascii_value)
        alphabet_dict[letter] = ascii_value - first_letter_value + 1

    return alphabet_dict


def repeat_n_times(letter, n):
    """
    Returns a string of letter n times in a row
    :param: letter: str
    :param: n: int
    :return str
    """
    repeated = ''
    for i in range(n):
        repeated += letter
    return repeated


def print_string_by_alphabet_order(string, alphabet_dict):
    """
    Prints out letters in a string a number of times from their place in the alphabet
    :param string: str, string to be printed
    :param alphabet_dict: dict, {'a':1, 'b':2, ...}
    """
    for letter in string:
        if letter == ' ':
            print('\n')
            continue

        # Our dictionary only has lower case letters for keys
        lower_case_letter = letter.lower()
        
        times_to_print = alphabet_dict[lower_case_letter]

        # Print the original letter, not the always lowercase version
        print(repeat_n_times(letter, times_to_print))


def main():
    alphabet_dict = get_alphbet_dict()
    print_string_by_alphabet_order('Foundry Spatial', alphabet_dict)


if __name__ == '__main__':
    main()
