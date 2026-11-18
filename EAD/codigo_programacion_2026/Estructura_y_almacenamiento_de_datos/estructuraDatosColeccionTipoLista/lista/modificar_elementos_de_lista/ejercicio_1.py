frutas=["manzana","pera","naranja","fresa"]#lista de frutas
print(frutas)#mostrar la lista
frutas[1]="kiwi"#reemplazar una fruta de la lista poniendo la pocision y la fruta a reemplazar
print(frutas)#mostrar de nuevo la lista
fruta_reemplazo=input("ingrese la fruta que desea reemplazar: ")#poner el nombre de la fruta a reemplazar
indice_fruta_a_reemplazar=frutas.index(fruta_reemplazo)#guarda la fruta indicada en un index
fruta_reemplazo=input("ingrese la fruta que desea reemplazar: ")#pone el nombre de la fruta que ira en la posicion de la fruta reemplazada
frutas[indice_fruta_a_reemplazar]=fruta_reemplazo#pone la fruta

print(frutas)#mostrar de nuevo la lista