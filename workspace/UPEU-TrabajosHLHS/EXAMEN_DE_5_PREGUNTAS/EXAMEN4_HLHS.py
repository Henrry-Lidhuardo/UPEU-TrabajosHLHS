#Definir Variable HLHS
Edad:float()
Genero:str()
Mensaje:str()
#Datos de Entrada HLHS
Edad=float(input("Ingrese la Edad: "))
Genero=str(input("Ingrese el Genero(Masculino o Femenino): "))
#Proceso HLHS
if Edad>=70:
    Mensaje:("C")
elif Edad>=16 and Edad<=69 and Genero=="Masculino" :
    Mensaje:("A")
elif Edad>=16 and Edad<=69 and Genero=="Femenino" :
    Mensaje:("B")
else:
    Mensaje:("A")
#Datos de Salida HLHS
print(f"La Vacuna que le Corresponde es: {Mensaje}")
