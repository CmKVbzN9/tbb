"""This is the third exercise"""
#!/usr/bin/env python3


def main():
    """This module creates quotes"""
    quote = str(input("What is the quote? "))
    said_by = str(input("Who said it? "))
    print('{} says, "{}".'.format(quote, said_by))

if __name__ == '__main__':
    main()
