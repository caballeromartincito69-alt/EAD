contraseña="A12"
intento=1
contraseñaingresar=input("ingrese una contraseña: ")
while contraseñaingresar != contraseña and intento <=3:
    contraseñaingresar=input("ingrese de nuevo la contraseña: ")
    intento=intento+1
if contraseñaingresar ==contraseña:
    print("contraseña correcta")
else:
    print("contraseña incorrecta")