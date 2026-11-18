myuser=input("ingrese su user: ")
mycontraseña=input("ingrese una contraseña: ")
attemps=0

user=input("ingrese su user: ")
contraseña=input("ingrese una contraseña: ")
while user !=myuser or contraseña != mycontraseña or attemps>=3:
    attemps+=1
    if user == myuser:
     print("usuario correcta")
     user=input("ingrese su user: ")
    elif contraseña==mycontraseña:
       print("contraseña correcta")
       contraseña=input("ingrese una contraseña: ")
    else:
     print("ha superado la cantidad de intentos permitidos,su usuario ha sido bloqueado")

if user == myuser and contraseña == mycontraseña:
   print("su usuario y contraseña son correctos, bienvenido al sistema")