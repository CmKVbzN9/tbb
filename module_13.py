"""This is the thirteenth exercise"""
#!/usr/bin/env python3


def main():
    """This module determines compound interest"""
    principle = int(input("What is the principal amount? "))
    rate = float(input("What is the rate "))
    years = int(input("What is the number of years? "))
    times = int(input("How many times is the interest compounded per year? "))
    interest = rate / 100
    total_value = principle * (1 + interest / times) ** (times * years)
    rounded_value = round(total_value, 2)
    print('{}$ is invested at {}%, for {} years componded {} times per year is ${}.'\
            .format(principle, rate, years, times, rounded_value))

if __name__ == '__main__':
    main()
