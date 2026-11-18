canciones={
    "cancion1":"windfall",
    "cancion2":"the show",
    "cancion3":"order", "cancion4":True
}
clave_nueva="cancion 6"
cancion_nueva=input("ingrese nuev cancion: ")
canciones["cancion 5"]="flower man"
canciones[clave_nueva]=cancion_nueva

print(canciones)

for clave,valor in canciones.items():
    print("_____________________________________________________")
    print(clave,"                ",valor)
    print("_____________________________________________________")