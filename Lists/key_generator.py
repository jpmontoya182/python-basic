import random


def generator():
    upper_dictionaty = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    lower_dictionary = ['a', 'b', 'c', 'd', 'e', 'x', 'y', 'z']
    symbols_dictionary = ['!', '@', '#', '$', '%']
    number_dictionary = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    characters = upper_dictionaty + lower_dictionary + \
        symbols_dictionary + number_dictionary

    password = []

    for i in range(15):
        password.append(random.choice(characters))

    return ''.join(password)


def run():
    password = generator()
    print('new password :' + password)


if __name__ == '__main__':
    run()
