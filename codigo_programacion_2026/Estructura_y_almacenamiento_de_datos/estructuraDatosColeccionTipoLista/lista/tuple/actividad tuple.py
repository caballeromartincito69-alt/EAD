materias=("ingles","matematicas","fvt","geografia","programacion")
materia_buscar=input("que materia desea buscar?: ")
if materia_buscar in materias:
 index=materias.index(materia_buscar)
 print(materia_buscar,"existe en la pocision", index)
else:
 print("no existe")