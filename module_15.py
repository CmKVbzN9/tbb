"""This is the fifteenth exercise"""
#!/usr/bin/env python3

def main():
    """This module validates passwords"""
    user_input = str(input("What is the password? "))
    password = "password"
    if user_input == password:
        print("Welcome!")
    else:
        print("I don't know you.")

if __name__ == '__main__':
    main()
