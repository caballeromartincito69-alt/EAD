answer=""
i=1
n=int(input("ingrese el numero de la tabla de multiplicar que deaea ejecutar: "))
while answer!="n":
    m=n*i
    print(n,"x",i,"=",m)
    i+=1
    answer=(input("desea continuar con la tabla del multiplicar?: y/n "))