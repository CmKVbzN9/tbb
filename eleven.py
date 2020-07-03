"""Currency Conversion"""
#!/usr/bin/env python3
import requests

def main():
    """Currency Conversion Module"""
    euros = int(input("How many euros are you exchanging? "))
    response = requests.get('https://api.exchangeratesapi.io/latest?symbols=USD')
    exchange_rate_response = response.json()
    rate = exchange_rate_response['rates']['USD']
    dollars = (euros * rate) / 1
    print(euros, "euros at an exchange rate of", rate, 'is {} U.S. dollars'.format(dollars))

if __name__ == '__main__':
    main()
