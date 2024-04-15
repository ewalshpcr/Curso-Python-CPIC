frase = input("Digite una frase cualquiera: ")
letra = input("Digite una letra cualquiera: ")
coincidencia = 0

for x in frase:
    if x == letra:
        coincidencia += 1

print(coincidencia)