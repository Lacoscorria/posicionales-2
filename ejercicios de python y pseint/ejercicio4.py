
placa1 = input("Ingrese la placa del primer bus: ")
pasajeros1 = int(input("Ingrese el número de pasajeros del primer bus: "))
valor_pasaje1 = float(input("Ingrese el valor del pasaje del primer bus: "))

recaudo1 = pasajeros1 * valor_pasaje1

placa2 = input("\nIngrese la placa del segundo bus: ")
pasajeros2 = int(input("Ingrese el número de pasajeros del segundo bus: "))
valor_pasaje2 = float(input("Ingrese el valor del pasaje del segundo bus: "))

recaudo2 = pasajeros2 * valor_pasaje2

print("\nResultado:")
if recaudo1 > recaudo2:
    print(f"El bus con placa {placa1} recogió más dinero: ${recaudo1:.2f}")
elif recaudo2 > recaudo1:
    print(f"El bus con placa {placa2} recogió más dinero: ${recaudo2:.2f}")
else:
    print(f"Ambos buses recogieron la misma cantidad de dinero: ${recaudo1:.2f}")