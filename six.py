"""This is a program that tells when you can retire"""
#!/usr/bin/env python3
from datetime import date

def main():
    """This is the retirement module"""
    age = int(input("What is your current age? "))
    retirement = int(input("At what age would you like to retire? "))
    years_left = retirement - age
    year = int(date.today().year)
    retirement_year = year + years_left
    print("You have", years_left, "years left until you can retire.")
    print("It's", year, 'so you can retire in, {}.'.format(retirement_year))

if __name__ == '__main__':
    main()
