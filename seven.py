"""This program calculates the area of a room"""
#!/usr/bin/env python3

def main():
    """This module does the math"""
    length = int(input("What is the length of the room in feet? "))
    width = int(input("What is the width of the room in feet? "))
    print("You entered dimensions of", length, "feet by", width, "feet.")
    print("The area is")

    conversion = 0.09290304
    feet = length * width
    meters = feet *conversion
    print(feet, "square feet")
    print(meters, "square meters")

if __name__ == '__main__':
    main()
