"""This is the sixth exercise"""
#!/usr/bin/env python3
from datetime import date

def main():
    """This module calculates retirement"""
    age = int(input("What is your current age? "))
    retirement = int(input("At what age would you like to retire? "))
    years_left = retirement - age
    year = int(date.today().year)
    retirement_year = year + years_left
    print("You have {}, years left until you can retire.".format(years_left))
    print("It's {}, so you can retire in, {}.".format(year, retirement_year))

if __name__ == '__main__':
    main()
