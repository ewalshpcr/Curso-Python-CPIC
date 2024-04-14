edadPersona = int(input("Digite su edad: "))

#for edad in range(1, edadPersona + 1):
for edad in range(1,edadPersona + 1):
    if edad == 0:
        print("En gestación")
    if edad == 1:
        print(edad,"año de edad")
    if edad > 1:
        print(edad,"años de edad")