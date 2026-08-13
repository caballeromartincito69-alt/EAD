nota=int(input("ingrese una nota"))
if nota >= 0 and nota < 7:
    print("la nota es insuficiente")

elif nota >=7 and nota < 10:
    print("la nota es suficiente")

elif nota == 10:
    print("la nota es excelente")

else:
    print("la nota es mayor de lo que se puede calcular")