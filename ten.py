"""Self-Checkout Program"""
#!/usr/bin/env python3


def main():
    """Self-Checkout Module"""
    item_one = int(input("Enter the price of item 1: "))
    quantity_one = int(input("Enter the quantity of item 1: "))
    item_two = int(input("Enter the price of item 2: "))
    quantity_two = int(input("Enter the quantity of item 2: "))
    item_three = int(input("Enter the price of item 3: "))
    quantity_three = int(input("Enter the quantity of item 3: "))
    subtotal = item_one * quantity_one + item_two * quantity_two + item_three * quantity_three
    tax = subtotal * .055
    total = tax + subtotal
    print('Subtotal: ${}'.format(subtotal))
    print('Tax: ${}'.format(tax))
    print('Total: ${}'.format(total))

if __name__ == '__main__':
    main()
