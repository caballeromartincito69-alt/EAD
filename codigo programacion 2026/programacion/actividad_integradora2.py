alimentos=["empanadas","ravioles"]
menu=int(input("seleccione una opcion:\n añadir un alimento a la lista \n insertar un elemento en la posicion 2 \n eliminar el elemento ingresando su nombre \n modificar un elemento de lsa lista ingresando su nombre y el nombre del elemento que lo reemplaza por teclado \n salir"))
if menu==1:
    alimento_nuevo=(input("ingrese el alimento a ingresar"))
    alimentos.append(alimento_nuevo)
elif menu==2:
 alimento_nuevo=(input("ingrese el alimento a añadir en la pocision 2 de la lista"))
 alimentos.insert(2,alimento_nuevo)
elif menu==3:
   alimento_borrar=(input("ingrese el alimento a eliminar por su nombre"))
   indice_alimento_a_borrar=alimentos.index(alimento_borrar)
   alimentos=[indice_alimento_a_borrar]=alimento_borrar
elif menu ==4:
   alimento_reemplazo=input("ingrese el libro que desea modificar: ")
   indice_libro_a_reemplazar=alimentos.index(alimento_reemplazo)
   alimento_reemplazo=input("ingrese la fruta que desea reemplazar: ")
   libro=[indice_libros_a_reemplazar]=alimento_reemplazo
elif menu==5:
   print("gracias por participar")