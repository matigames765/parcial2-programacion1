
'''Magneto quiere reclutar la mayor cantidad de mutantes para poder 
luchar contra los X-Mens.

Te ha contratado a ti para que desarrolles un programa que detecte 
si un humano es mutante basándose en su secuencia de ADN.

Para eso te ha pedido crear un programa con un método o función booleana,
llamada is_mutant(dna), que recibe como parámetro un arreglo de Strings que
representan cada fila de una matriz 6x6 con la secuencia de ADN.

Las letras de los Strings solo pueden ser: A,T,C,G; las cuales representan 
cada base nitrogenada del ADN.

Sabrás si un humano es mutante, si encuentras más de una secuencia de 
cuatro letras iguales, estas pueden aparecer de forma oblicua, horizontal 
o vertical. '''
import funciones_magneto
#Ciclo while principal del programa que se cortara cuando el usuario desee
while True:
    mutant_matrix = []
    string_mutant = "ATCG" 
    print("Ahora vas a ingresar 6 strings de 6 caracteres")
    print("Estos representaran la secuencia de adn del mutante o no mutante!")
    #Funcion para crear la matriz
    funciones_magneto.creating_matrix(mutant_matrix,string_mutant)
    #Funcion para saber si la matriz es de un mutante
    mutant_secuence = funciones_magneto.is_mutant(mutant_matrix)
    if (mutant_secuence >= 2):
        print("El humano es un mutante, servira para luchar contra los X-MEN!")
    else:
        print("El humano lamentablemente no es un mutante")
    out = input("Ingresa 1 si deseas salir o cualquier otra tecla para reiniciar el programa: ")
    if (out == "1"):
        print("Programa finalizando, adios!...")
        break
    else:
        pass