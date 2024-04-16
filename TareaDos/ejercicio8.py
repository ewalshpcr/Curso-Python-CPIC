numero = int(input("Digite un número entero positivo, sin decimales: "))

def esNumeroPrimo(numeroAConsultar):
    contador = 0

    for entero in range(2, numeroAConsultar):
        if numeroAConsultar % entero == 0:
            contador += 1

    #Cumpliendo la regla que sean divisibles solo por ellos mismo y 1
    if (numeroAConsultar % 1 == 0) and (numeroAConsultar % numeroAConsultar == 0) and contador == 0:
        print(f"El número {numeroAConsultar} es primo")
    else:
        print(f"El número {numeroAConsultar} No es primo")

esNumeroPrimo(numero)

#for x in range(2, 101):
#    esNumeroPrimo(x)
