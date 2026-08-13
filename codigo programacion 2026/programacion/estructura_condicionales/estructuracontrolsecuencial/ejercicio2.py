#Actividad: Escribir un programa que solicite el precio de 2 productos, los sume y muestre el precio total con el descuento del 10%
precio_producto_1 = float(input("ingrese el precio del producto: "))
#ingresamos el precio del 2do producto

precio_producto_2 = float(input("ingrese el precio del segundo producto: "))
#aplicamos el descuento

descuento1 = precio_producto_1 - (precio_producto_1 * 0.10)
#aplicamos el descuento al 2do producto

descuento2 = precio_producto_2 - (precio_producto_2 * 0.10)
#hacemos el descuento final

descuento_final = (descuento1 + descuento2)
#mostramos el precio final

print("su precio final con descuento del 10% es de: ",descuento_final)