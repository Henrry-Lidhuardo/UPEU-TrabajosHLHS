def EXAMEN1_HLHS():
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

def EXAMEN2_HLHS():
    #Definir Variable HLHS
    Igv:float()
    Descuento:float()
    Pbase:float()
    Mtotal:float()
    PrecioFinal:float()
    #Datos de Entrada HLHS
    Pbase=float(input("Ingrese el Precio Base: "))
    #Proceso HLHS
    if Pbase>=2000:
        Descuento=Pbase*0.10
    elif Pbase>=1000 and Pbase<2000:
        Descuento=Pbase*0.5
    elif Pbase>=500 and Pbase<1000:
        Descuento=Pbase*0.2
    else:
        Descuento=0
    PrecioFinal=Pbase-Descuento
    Igv=PrecioFinal*0.18
    Pfinal=PrecioFinal+Igv
    #Datos de Salida HLHS
    print(f"El Descuento es: {Descuento}")
    print(f"El Igv es: {Igv}")
    print(f"El Precio Final es: {Pfinal}")

def EXAMEN3_HLHS():
    #Definir Variables HLHS
    Dato1:float()
    Dato2:float()
    Signo:str()()
    Total:float()
    #Datos de Entrada HLHS
    Dato1=float(input("Ingrese el Dato 1: "))
    Dato2=float(input("Ingrese el Dato 2: "))
    print("- = Resta ")
    print("+ = Suma ")
    print("/ = Dividir ")
    print("* = Multiplicar ")
    print("^ = Potencia ")
    print("R = Raiz")
    print("% = Potencia")
    signo=str(input("Ingrese el Signo: "))
    #Proceso HLHS
    if Signo=="+": 
        Total=Dato1+Dato2
    elif Signo=="-": 
        Total=Dato1-Dato2
    elif Signo=="/":
        Total=Dato1/Dato2
    elif Signo=="*":
        Total=Dato1*Dato2
    elif Signo=="^":
        Total=Dato1^Dato2
    elif Signo=="R":
        Total=Dato1*(Dato2*-1)
    else :
        Total=Dato1%Dato2
    #Datos de Salida HLHS
    print(f"La Respuesta es: {Total}")

def EXAMEN4_HLHS():
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

#EXAMEN_DE_5_PREGUNTAS
#Definir Variables
Numero = float
#Datos de entrada
Numero = float ( input ( "Ingrese el Numero del Ejercicio(1-4): " ))
#Proceso
if Numero==1:
    EXAMEN1_HLHS()
elif Numero==2:
    EXAMEN2_HLHS()
elif Numero==3:
    EXAMEN3_HLHS()
else :
    EXAMEN4_HLHS()
