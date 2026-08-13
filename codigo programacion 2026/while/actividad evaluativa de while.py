numero=9
intentos=1
adivinar=int(input("adivina el numero: "))
while adivinar!=numero or intentos <=3:
    intentos= intentos+1 
    adivinar=int(input("intente otra vez: "))
if adivinar == numero:
 print("felicidades,el numero era el",numero)
if intentos <=3:
   print("excedio el limite de intentos")
