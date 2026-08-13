paises=["Argentina"]
respuesta=input("desea agregar un pais a lista si o no: ")
if respuesta == "si":
    pocision=input("desea agregar el pais en una pocision especifica si o no?: ")
    if pocision == "si":
     pos=int(input("ingresar la pocision donde desea agregar el nuevo elemento"))
     pais_nuevo=input("ingrese el nombre del pais a agregar: ")
     paises.insert(pos,pais_nuevo)
     print(paises)
    else:
     pais_nuevo=input("ingrese el nombre del pais a agregar: ")
     paises.append(pais_nuevo)
     print(paises)
else:
    print("Fin del servicio")
    print(paises)