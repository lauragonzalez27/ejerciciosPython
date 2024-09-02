"Leer 20 números e imprimir cuantos son positivos, cuantos negativos y cuantos neutros"
#estos son los contadores 
numerosPositivos=0
numerosNegativos=0
numerosNeutros=0

#se inicia el ciclo for

for x in range (20):
    numero= int(input(f"ingrese el numero {x+1}: "))
    # se suma los numeros de cada contador 
    if numero > 0:
        numerosPositivos +=1   
    elif numero < 0:
        numerosNegativos +=1
    else:
        numerosNeutros += 1


#imprime los datos 
print(f"son numeros positivos {numerosPositivos}") 
print(f"son numeros negativos {numerosNegativos}")
print(f"numeros neutros {numerosNeutros}")