#Actividad:escribir un programa que solicite ingresar el precio de un producto y le reste el 10%, luego mostrar el precio final

#solicitar al usuario ingresar el precio del producto
precio_producto = float(input("ingrese el precio del producto: "))


#calculamos el descuento del 10%
descuento = precio_producto - (precio_producto * 0.10)

#mostrar precio final con descuento del 10%
print("su precio final con descuento del 10% es de: ",descuento)