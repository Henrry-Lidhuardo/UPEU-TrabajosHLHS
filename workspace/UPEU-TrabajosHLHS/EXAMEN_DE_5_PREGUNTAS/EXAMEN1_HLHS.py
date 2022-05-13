#Definir Variables HLHS
Excon:float()
Test:float()
Entrevista:float()
Cexcon:float()
Ctest:float()
Centrevista:float()
Notafinal:float()
Nota:float()
Nivel:str()
#Datos de Entrada HLHS
Excon=float(input("Ingrese la Calificacion del Examen de Conocimiento: "))
Test=float(input("Ingrese la Calificacion del Examen Psicologico: "))
Entrevista=float(input("Ingrese la Calificacion de la Entrevista Personal: "))
#Proceso HLHS
Cexcon=Excon*0.40
Ctest=Test*0.35
Centrevista=Entrevista*0.25
Notafinal=Cexcon+Ctest+Centrevista
if Notafinal>=17:
    Nivel=("4")
if Notafinal<17 and Notafinal>=14:
    Nivel=("3")
if Notafinal<14 and Notafinal>=11:
    Nivel=("No Puede Obtener la Vacante y Esta en el Nivel 1:")
#Datos de Salida HLHS
print(f"La Nota Final es: {Notafinal} ")
print(f"Su Nivel es: {Nivel}")
