import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elija un numero entre 1 y 100 : '))

    while numero_elegido != numero_aleatorio:
        if numero_elegido < numero_aleatorio:
            print('El numero es mayor')
        else:
            print('El numero es menor')

        numero_elegido = int(input('Ingresa de nuevo: '))

    print('!Ganaste')


if __name__ == '__main__':
    run()
