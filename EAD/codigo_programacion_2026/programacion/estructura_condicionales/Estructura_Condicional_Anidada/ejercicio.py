num=int(input("ingresa un numero: "))
if num>-10 and num<10:
    print("el numero ingresado tiene un solo digito")
#else if
elif num>=10 and num<100 and num>-100:
    print("el numero ingresado tiene 2 digitos")
elif num>=100 and num<1000 and num>-1000:
    print("el numero ingresado tiene 3 digitos")
else:
    print("el numero ingresado tiene mas de 3 digitos")