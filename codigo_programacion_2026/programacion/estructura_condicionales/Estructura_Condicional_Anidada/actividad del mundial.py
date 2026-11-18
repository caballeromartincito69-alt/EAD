argentina=[]
alemania=[]
mexico=[]
sudafrica=[]
checoslovaquia=[]
korea_del_norte=[]
suiza=[]
canada=[]
qatar=[]
Bosnia_y_Herzegovina=[]
escosia=[]
marruecos=[]
brasil=[]
haiti=[]
estados_unidos=[]
australia=[]
turquia=[]
paraguay=[]
costa_de_marfil=[]
ecuador=[]
curazao=[]
japon=[]
paises_bajos=[]
suecia=[]
tunez=[]
nueva_zelanda=[]
iran=[]
belgica=[]
egipto=[]
uruguay=[]
arabia_saudi=[]
españa=[]
cavo_verde=[]
noruega=[]
francia=[]
senegal=[]
irak=[]
austria=[]
jordania=[]
argelia=[]
colombia=[]
la_republica_del_congo=[]
portugal=[]
uzbekistan=[]
inglaterra=[]
ghana=[]
panama=[]
croacia=[]

puntos=input("desea agregar puntos a un equipo si/no")
while puntos=="si":
    elegir_equipo=input("ingrese nombre del equipo, presione s para salir")
    elegir_equipo.upper()
    if elegir_equipo=="ARGENTINA":
        new_points=int(input("ingrese puntos a añadir"))
        argentina.append(new_points)
        print(argentina.sum())
    elif elegir_equipo=="ALEMANIA":
        new_points=int(input("ingrese puntos a añadir"))
        alemania.append(new_points)
        print(alemania.sum())
    elif elegir_equipo=="MEXICO":
        new_points=int(input("ingrese puntos a añadir"))
        mexico.append(new_points)
        print(mexico.sum())
    elif elegir_equipo=="SUDAFRICA":
        new_points=int(input("ingrese puntos a añadir"))
        sudafrica.append(new_points)
        print(sudafrica.sum())
    elif elegir_equipo=="CHECOSLOVAQUIA":
        new_points=int(input("ingrese puntos a añadir"))
        checoslovaquia.append(new_points)
        print(checoslovaquia.sum())
    elif elegir_equipo=="S":
        puntos="no"
        print("gracias por participar")