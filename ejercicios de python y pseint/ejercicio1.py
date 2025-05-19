
hermano1_nombre = input("Ingresa el nombre del primer hermano: ")
hermano1_edad = int(input(f"Ingresa la edad de {hermano1_nombre}: "))

hermano2_nombre = input("Ingresa el nombre del segundo hermano: ")
hermano2_edad = int(input(f"Ingresa la edad de {hermano2_nombre}: "))


if hermano1_edad > hermano2_edad:
    print(f"{hermano1_nombre} es mayor que {hermano2_nombre}.")
elif hermano2_edad > hermano1_edad:
    print(f"{hermano2_nombre} es mayor que {hermano1_nombre}.")
else:
    print(f"{hermano1_nombre} y {hermano2_nombre} tienen la misma edad.")