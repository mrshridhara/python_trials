"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

https://projecteuler.net/problem=1
"""


def get_multiples_of_3_or_5(limit):
    for i in range(limit):
        if i % 3 == 0 or i % 5 == 0:
            yield i


def run(limit):
    print('Sum of all the multiples of 3 or 5 below {}:'.format(limit))
    print(sum(get_multiples_of_3_or_5(limit)))


if __name__ == '__main__':
    run(1000)