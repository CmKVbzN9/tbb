"""This is a program that does simple math"""
#!/usr/bin/env python3


def main():
    """This is the math module"""
    first_number = int(input("What is the first number? "))
    second_number = int(input("What is the second number? "))
    print("{} + {}".format(first_number, second_number), " = ", first_number+second_number)
    print("{} - {}".format(first_number, second_number), " = ", first_number-second_number)
    print("{} * {}".format(first_number, second_number), " = ", first_number*second_number)
    print("{} / {}".format(first_number, second_number), " = ", first_number/second_number)

if __name__ == '__main__':
    main()
