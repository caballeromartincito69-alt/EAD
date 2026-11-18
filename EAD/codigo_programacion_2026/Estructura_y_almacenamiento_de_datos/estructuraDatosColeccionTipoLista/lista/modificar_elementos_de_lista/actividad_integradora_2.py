libros=["harry_potter","el_principito","la_biblia"]#la lista de libros
print(libros)#muestra la lista de libros
libros.append("don quijote de la mancha")#pone un libro al final de la lista
libros.insert(0,"el caballero de la armadura oxidada")#pone un libro al principio de la lista
print(libros)#muestra la lista de libros
libros.pop(2)#quita el libro que esta en la pocision 2
libros_borrar=input("ingrese el libro que desea eliminar: ")#pregunta que libro desea eliminar por su nombre
libros.remove(libros_borrar)#borra el libro
print(libros)#muestra la lista de libros
libros.insert(2,"el señor de los anillos")#pone un libro en la pocision 2 de la lista
print(libros)#muestra la lista de libros
libro_modificar=input("ponga el nombre del libro a poner en la posicion 1")#pregunta que libro poner en la pocision 1
libros.insert(1,libro_modificar)#pone el libro mencionado antes en la pocision 1
print(libros)#muestra la lista de libros
libros_reemplazo=input("ingrese el libro que desea modificar: ")#pregunta que libro se quiere modificar por su nombre
indice_libro_a_reemplazar=libros.index(libros_reemplazo)#guarda el libbro en un index
libros_reemplazo=input("ingrese la fruta que desea reemplazar: ")#pregunta el libro que se quiera poner en el lugar del libro que se quiere modificar
libro=[indice_libros_a_reemplazar]=libros_reemplazo#pone el libro y lo reemplaza
print(libros)#mostrar la lista de libros