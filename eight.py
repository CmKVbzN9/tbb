"""Pizza Party"""
#!/usr/bin/env python3


def main():
    """Pizza Party Module"""
    people = int(input("How many people? "))
    pizza = int(input("How many pizzas do you have? "))
    slices = pizza * 8
    slices_per_person = slices // people
    leftover = slices % people
    print(people, "people with", pizza, "pizzas")
    print("Each person gets", slices_per_person, "pieces of pizza.")
    print("There are", leftover, "leftover pieces.")

if __name__ == '__main__':
    main()
