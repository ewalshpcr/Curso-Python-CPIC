numero = int(input("Digite un numero que se mayor que cero y sin decimales: "))

for reverso in reversed(range((numero + 1))):
    print(reverso, end=', ')
