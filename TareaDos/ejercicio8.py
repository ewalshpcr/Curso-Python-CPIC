numero = int(input("Digite un número entero positivo, sin decimales: "))

def esNumeroPrimo(numeroAConsultar):
    contador = 0

    for entero in range(1, (numeroAConsultar + 1)):
        #print(numeroAConsultar, entero)
        if numeroAConsultar % entero == 0:
            contador += 1

    if contador == 2:
        print(f"El número {numeroAConsultar} es primo")
    else:
        print(f"El número {numeroAConsultar} No es primo")

esNumeroPrimo(numero)