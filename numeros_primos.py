def es_primo(numero):
    result = True
    # contador = 0
    for i in range(1, numero + 1):
        print(i)
        if i == 1 or i == numero:
            continue
        if numero % i == 0:
            result = False
            break
    #     if i == 1 or i == numero:
    #         continue
    #     if numero % i == 0:
    #         contador += 1

    # if contador == 0:
    #     return True
    # else:
    #     return False

    return result


def run():
    numero = int(input('Ingrese un numero para el calculo : '))

    if es_primo(numero):
        print('El numero ingresado es primo')
    else:
        print('El numero ingresado no es primo')


if __name__ == '__main__':
    run()
