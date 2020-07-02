#!/usr/bin/env python3
"""This counts characters"""

def main():
    """This is a character counting module"""
    user_input = str(input("What is the input string? "))
    print(user_input + " has " + str(len(user_input)) + " characters.")
