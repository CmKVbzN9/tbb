"""This is the twelth exercise"""
#!/usr/bin/env python3


def main():
    """This module computes simple interest"""
    principle = int(input("Enter the principal: "))
    rate = float(input("Enter the rate of interest: "))
    years = int(input("Enter the number of years: "))
    interest = rate / 100
    total = principle * (1 + interest * years)
    print("After {} years at {}%, the investment will be worth ${}.".format(years, rate, total))

if __name__ == '__main__':
    main()
