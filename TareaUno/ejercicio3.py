cantidadAInvertir = float(input("Digite la cantidad a invertir: "))
interesAnual = float(input("Digite el interés anual: "))
numeroAnhos = int(input("Digite el número de años de la inversión: "))

capital = cantidadAInvertir*(((interesAnual/100) + 1)**numeroAnhos)

print("El capital resultado de la inversión es: ", capital)