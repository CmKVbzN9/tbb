"""This program calculates tax"""
#!/usr/bin/env python3


def main():
    """This module does the calculation"""
    order_amount = int(input("What is the order amount? "))
    state = str(input("What is the state? "))
    tax = 1.055
    taxed = order_amount * tax
    rounded = round(taxed, 2)
    if state == 'WI':
        print("The subtotal is ${}.".format(order_amount))
        print("The tax is $0.55.")
        print("The total is ${}.".format(rounded))
    else:
        print("The total is ${}.".format(order_amount))

if __name__ == '__main__':
    main()
