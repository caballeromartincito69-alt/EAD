lista_peliculas=["spider man 3","El jorobado de Notre Dame","kung fu panda","minions","hombres de negro","michael jackson"]
print(lista_peliculas)
lista_peliculas.pop()
ingesar_nombre=(input("desea ingresar una pelicula a la lista?: "))
lista_peliculas.append(ingesar_nombre)
lista_peliculas.pop(2)
ingesar_nombre_2=(input("desea remover una pelicula de la lista?: "))
if ingesar_nombre_2 == "si":
    quitar_peli=input("nombre de la pelicula a remover")
    lista_peliculas.remove(quitar_peli)
    print(lista_peliculas)
lista_peliculas.insert(2,ingesar_nombre)
print(lista_peliculas)