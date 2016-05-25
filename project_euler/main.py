"""
Entry point of the application.
"""


def try_run(module, arg):
    try:
        module.run(arg)
    except Exception as e:
        print('Error: {}'.format(e))


print('Project Euler (https://projecteuler.net/)')

options = [('1', 'Multiples of 3 and 5'),
           ('2', 'Even Fibonacci Numbers'),
           ('3', 'Largest Prime Factor'),
           ('4', 'Largest Palindrome Product'),
           ('q', 'Quit')]

while True:
    print('\nChoose one of the below:')
    for option, name in options:
        print(option, ':', name)
    choice = input('\nYour choice:')

    if choice == 'q' or choice == 'Q':
        break

    elif choice == '1':
        import multiples_of_3_and_5
        limit = int(input('Enter the limit: '))
        try_run(multiples_of_3_and_5, limit)

    elif choice == '2':
        import even_fibonacci_numbers
        limit = int(input('Enter the limit: '))
        try_run(even_fibonacci_numbers, limit)

    elif choice == '3':
        import largest_prime_factor
        num = int(input('Enter a number: '))
        try_run(largest_prime_factor, num)

    elif choice == '4':
        import largest_palindrome_product
        digits = int(input('Enter number of digits: '))
        try_run(largest_palindrome_product, digits)

    else:
        print('Invalid input!')