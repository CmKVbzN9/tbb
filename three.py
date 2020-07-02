"""This is a program that prints quotes"""
#!/usr/bin/env python3


def main():
    """This is a quote creation module"""
    quote = str(input("What is the quote? "))
    said_by = str(input("Who said it? "))
    print(said_by + " says, " + "\"" + quote + "\"")
