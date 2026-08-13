valor_contraseña=int(input("ingrese un valor para la contraseña: "))
verificar_contraseña=int(input("ingrese de nuevo la contraseña: "))
if valor_contraseña == verificar_contraseña:
    print("bienvenido usuario")

else:
    print("la contraseña ingresada es incorrecta")
