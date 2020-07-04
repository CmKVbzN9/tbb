"""This is the eleventh exercise"""
#!/usr/bin/env python3
import requests

def main():
    """This module converts euros to dollars"""
    euros = int(input("How many euros are you exchanging? "))
    response = requests.get('https://api.exchangeratesapi.io/latest?symbols=USD')
    exchange_rate_response = response.json()
    rate = exchange_rate_response['rates']['USD']
    dollars = (euros * rate) / 1
    print("{} euros at an exchange rate of {} is {} U.S. dollars".format(euros, rate, dollars))

if __name__ == '__main__':
    main()
