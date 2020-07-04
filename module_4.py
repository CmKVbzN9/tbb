"""This is the fourth exercise"""
#!/usr/bin/env python3


def main():
    """This module does a mad lib"""
    noun = str(input("Enter a noun: "))
    verb = str(input("Enter a verb: "))
    adjective = str(input("Enter a adjective: "))
    adverb = str(input("Enter a adverb: "))
    print("Do you {} your {} {} {}? Thats dank.".format(verb, adjective, noun, adverb))

if __name__ == '__main__':
    main()
