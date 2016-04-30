"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

https://projecteuler.net/problem=3
"""


def get_prime_factors(num):
    div = 2
    while num > 1:
        while num % div == 0:
            yield div
            num //= div
        div += 1
        if div * div > num:
            if num > 1:
                yield num
            break


def get_largest_prime_factor(num):
    if num < 3:
        return num
    return max(get_prime_factors(num))


def run(num):
    print('Largest prime factor of {}:'.format(num))
    print(get_largest_prime_factor(num))


if __name__ == '__main__':
    run(600851475143)