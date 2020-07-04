"""This is the second exercise"""
#!/usr/bin/env python3


def main():
    """This module counts the number of characters in a string"""
    user_input = str(input("What is the input string? "))
    string_length = str(len(user_input))
    print("{} has {} characters.".format(user_input, string_length))

if __name__ == '__main__':
    main()
