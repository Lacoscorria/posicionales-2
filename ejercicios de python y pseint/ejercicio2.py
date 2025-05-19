print("ingrese la edad")
edad=int(input("ingrese su edad"))
if edad<10:
    print ("es un niño")
elif edad>10 and edad<15:
    print("es un preadolescente")
elif edad>15 and edad<18:
    print("es un adolescente")
elif edad>18 and edad<50:
    print("es un adulto")
elif edad>50 and edad<150:
    print("es un adulto mayor")   
elif edad>150:
    print("esta muerto")    