"""
Problem: https://projecteuler.net/problem=1

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
    The sum of these multiples is 23.

    Find the sum of all the multiples of 3 or 5 below 1000.
"""


def get_multiples_of_3_or_5(limit):
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            yield i


if __name__ == '__main__':
    print(__doc__)
    solution = sum(get_multiples_of_3_or_5(1000))
    print('Solution: {}'.format(solution))
