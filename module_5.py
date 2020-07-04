"""This is the fifth exercise"""
#!/usr/bin/env python3


def main():
    """This module does simple math"""
    first_number = int(input("What is the first number? "))
    second_number = int(input("What is the second number? "))
    print("{} + {}".format(first_number, second_number), " = ", first_number+second_number)
    print("{} - {}".format(first_number, second_number), " = ", first_number-second_number)
    print("{} * {}".format(first_number, second_number), " = ", first_number*second_number)
    print("{} / {}".format(first_number, second_number), " = ", first_number/second_number)

if __name__ == '__main__':
    main()
