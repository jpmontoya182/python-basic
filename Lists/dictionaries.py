def run():
    mi_diccionario = {
        'name': 'juan',
        'isStudent': False,
        'age': 37
    }
    # print(mi_diccionario['age'])
    # print(mi_diccionario)

    # for elements in mi_diccionario.keys():
    #     print(elements)

    # for elements in mi_diccionario.values():
    #     print(elements)

    for elem, value in mi_diccionario.items():
        print('The element: ' + elem + ', has a value: ' + str(value))


# entrypoint
if __name__ == '__main__':
    run()
