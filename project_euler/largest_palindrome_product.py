"""
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.

https://projecteuler.net/problem=4
"""


def get_largest_palindrome_product(limit):
    raise NotImplementedError()


def run(digits):
    print('Largest palindrome product of {} digits:'.format(digits))
    print(get_largest_palindrome_product(digits))   


if __name__ == '__main__':
    run(3)