def run():
    # for contador in range(100):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(100):
    #     print(i)
    #     if i == 56:
    #         break

    texto = input('Ingrese un texto : ')
    for letra in texto:
        print(letra)
        if letra == 'o':
            break


if __name__ == '__main__':
    run()
