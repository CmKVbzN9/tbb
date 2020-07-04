"""This is the ninth exercise"""
#!/usr/bin/env python3


def main():
    """This module calculates how much paint you need fo the ceiling of a room"""
    length = int(input("Length? "))
    width = int(input("Width? "))
    area = length * width
    paint = area / 350
    print("You will need to purchase {} gallons of paint to cover {} square feet."\
            .format(paint, area))

if __name__ == '__main__':
    main()
