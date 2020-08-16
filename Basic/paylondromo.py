def palindromo(palabra):
    palabra = palabra.replace(' ', '').strip().lower()
    palabra_invertida = palabra[::-1]
    if palabra == palabra_invertida:
        return True
    else:
        return False


def run():
    palabra = input('Escribe una palabra a evaluar : ')
    es_palindromo = palindromo(palabra)
    if es_palindromo == True:
        print('la palabra ingresada es un palindromo')
    else:
        print('la palabra ingresada no es un palindromo')


if __name__ == '__main__':
    run()
