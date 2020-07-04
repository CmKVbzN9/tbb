"""This is the seventh exercise"""
#!/usr/bin/env python3

def main():
    """This module calculates the area of a rectangular room"""
    length = int(input("What is the length of the room in feet? "))
    width = int(input("What is the width of the room in feet? "))
    conversion = 0.09290304
    feet = length * width
    meters = feet *conversion
    print("You entered dimensions of {} feet by {} feet.".format(length, width))
    print("The area is")
    print("{} square feet".format(feet))
    print("{} square meters".format(meters))

if __name__ == '__main__':
    main()
