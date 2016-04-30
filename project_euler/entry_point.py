"""
Entry point of the application.
"""

options = [('1', 'Multiples of 3 and 5'),
           ('2', 'Even Fibonacci Numbers'),
           ('3', 'Largest Prime Factor'),
           ('q', 'Quit')]

while True:
    print('\nChoose one of the below:')
    for option, name in options:
        print(option, ': ', name, sep = '')
    choice = input('\nYour choice:')

    if choice == '1':
        import multiples_of_3_and_5
        limit = int(input('Enter the limit: '))
        multiples_of_3_and_5.run(limit)

    elif choice == '2':
        import even_fibonacci_numbers
        limit = int(input('Enter the limit: '))
        even_fibonacci_numbers.run(limit)

    elif choice == '3':
        import largest_prime_factor
        num = int(input('Enter a number: '))
        largest_prime_factor.run(num)

    elif choice == 'q' or choice == 'Q':
        break

    else:
        print('Invalid input!')