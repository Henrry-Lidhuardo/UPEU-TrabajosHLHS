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
