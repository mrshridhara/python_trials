"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

https://projecteuler.net/problem=3
"""

def get_factors(num):
    for i in range(num - 1):
        if i != 0 and i != 1 and num % i == 0:
            yield i 

def is_prime_number(num):
    if len(list(get_factors(num))) == 0:
        return True
    else:
        return False

def get_prime_factors(num):
    for f in get_factors(num):
        if is_prime_number(f):
            yield f

def get_larget_prime_factor(num):
    return max(get_prime_factors(num))

def run(num):
    print('Largest prime factor of ' + str(num) + ':')
    print(get_larget_prime_factor(num))

if __name__ == '__main__':
    run(600851475143)