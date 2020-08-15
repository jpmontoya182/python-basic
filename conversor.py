menu = """
This the current conversion 😊

1 - Colombian pesos
2 - Argetine pesos
3 - Mexican pesos

Chose an option :
"""

option = input(menu)


def conversion(pesos_convert, dollar_value):
    return str(round(pesos_convert / dollar_value, 2))


if option == '1':
    pesos = input("how many Colombian pesos do you have ? : ")
    dollar_value = 3850
    dollar = conversion(float(pesos), dollar_value)
    print("You have : " + dollar + " dollars")
elif option == '2':
    pesos = input("how many Argentine pesos do you have ? : ")
    dollar_value = 65
    dollar = conversion(float(pesos), dollar_value)
    print("You have : " + dollar + " dollars")
elif option == '3':
    pesos = input("how many Mexican pesos do you have ? : ")
    dollar_value = 400
    dollar = conversion(float(pesos), dollar_value)
    print("You have : " + dollar + " dollars")
else:
    print('Could you select a valid option please')
