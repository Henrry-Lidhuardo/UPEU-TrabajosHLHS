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
