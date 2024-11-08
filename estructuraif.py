"""
condicionales if:
 evaluan expresiones booleanas
estructura:
 if expresion:
     instrucciones 
else:
    instrucciones
if expresion: 
 instrucciones
elif expresion:
 instrucciones
else:
 instrucciones
"""
print("programa que verifica si un numero es posotivo")
num = int(input("ingresa un numero: "))
# preguntar el numero es mayor 0:
if num > 0:
     print("el numero es positivo")
     print("fin del programa")