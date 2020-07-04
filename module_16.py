"""This is the sixteenth exercise"""
#!/usr/bin/env python3

def main():
    """This module determines if you can legally drive"""
    age = int(input("What is your age? "))
    legal = 16
    if age >= legal:
        print("You are old enough to legally drive.")
    elif age < legal:
        print("You are not old enough to legally drive.")

if __name__ == '__main__':
    main()
