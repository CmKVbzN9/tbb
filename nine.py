"""Paint Calculator"""
#!/usr/bin/env python3


def main():
    """Paint Calculator Module"""
    length = int(input("Length? "))
    width = int(input("Width? "))
    area = length * width
    paint = area / 350
    print("You will need to purchase", paint, "gallons of paint to cover", area, "square feet.")

if __name__ == '__main__':
    main()
