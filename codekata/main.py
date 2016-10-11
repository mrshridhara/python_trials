"""
Entry point of the application.
"""


def try_run(module):
    try:
        module.run()
    except Exception as e:
        print('Error: {}'.format(e))


print('CodeKata (http://codekata.com/)')

options = [('1', 'Supermarket Pricing'),
           ('q', 'Quit')]

while True:
    print('\nChoose one of the below:')
    for option, name in options:
        print(option, ':', name)
    choice = input('\nYour choice:')

    if choice == 'q' or choice == 'Q':
        break

    elif choice == '1':
        import supermarket_pricing
        try_run(supermarket_pricing)

    else:
        print('Invalid input!')
