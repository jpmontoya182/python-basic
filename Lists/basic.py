objetos = ['juan', 1, 4.5, True]
print(objetos)

objetos.append(5)
objetos.append(False)
print(objetos)

objetos.pop(1)
print(objetos)

for element in objetos:
    print(element)

# ---------------------------------
numero = [1, 2, 3, 4]
numero_dos = [5, 6, 7]
lista_final = numero + numero_dos

tupla = (1, 2, 3, 4, 5)
# tupla is a readonly / inmmutable list, is more efficient with bucles. It does not
# allowed the append and pop
