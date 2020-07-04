"""This is the eigth exercise"""
#!/usr/bin/env python3


def main():
    """This module calculates how many slices of pizza people get at a pizza party"""
    people = int(input("How many people? "))
    pizza = int(input("How many pizzas do you have? "))
    slices = pizza * 8
    slices_per_person = slices // people
    leftover = slices % people
    print("{} people with {} pizzas".format(people, pizza))
    print("Each person gets {} pieces of pizza.".format(slices_per_person))
    print("There are {} leftover pieces.".format(leftover))

if __name__ == '__main__':
    main()
