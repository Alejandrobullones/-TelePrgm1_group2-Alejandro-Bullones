print("5.1 Defina una función en python que acepte el radio y devuelva el valor del area de un círculo de esas dimensiones. (4pts)")




import math

vRadio = int(input("intruduzca el radio:"))

def circulo(vRadio):
    area = math.pi * vRadio ** 2
    return area

print(circulo(vRadio))
print("El primer ejercicio está finalizado, vamos al siguiente")

print("5.2 Defina una función en python que acepte 3 valores y devuelva solo el maximo de los tres")

valor1 = int(input("introduzca el primer valor:"))
valor2 = int(input("introduzca el segundo valor:"))
valor3 = int(input("introduzca el tercer valor:"))
valores = [valor1, valor2, valor3]

def valorMaximo(valores):
    mayor = valores[0]

    for i in range(1, len(valores)):
        if valores[i] > mayor:
            mayor = valores[i]
    return mayor        

print("El valor máximo es:", valorMaximo(valores))
print("El segundo ejercicio está finalizado, vamos al siguiente")

print("Dado una lista de enteros,defina una función en python que devuelva la suma de solo los valores impares de dicha lista. (7pts)")

valor1 = int(input("Introduza valor uno:"))
valor2 = int(input("Introduza valor dos:"))
valor3 = int(input("Introduza valor tres:"))
valor4 = int(input("Introduza valor cuatro:"))
valor5 = int(input("Introduza valor cinco:"))
valor6 = int(input("Introduza valor seis:"))

numeros = [valor1,valor2,valor3,valor4,valor5,valor6]

    
def resultado(numeros):
    impar = 0
    for i in range(len(numeros)):
        if numeros[i] % 2 == 1:
            impar = impar + numeros[i]
    
    return impar


print("la suma es de los valores impares es: ", resultado(numeros))
print("El tercer ejercicio está finalizado, vamos al siguiente")

def texto ():
    textoPrueba = 'alejandro'
    caracteresTotales = 30 % 2
    centrado = len(textoPrueba) - caracteresTotales
    retorno = textoPrueba + '. la cantidad de carateres para el centrado del texto es:' + str(centrado)
    return retorno

print('el texto inicial es: ', texto())

print("El cuarto ejercicio está finalizado, los ejercicios han finalizado")






