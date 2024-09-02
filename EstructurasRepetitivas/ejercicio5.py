"Una persona debe realizar un muestreo con 50 personas para determinar el promedio de peso de los niños,"
"jóvenes, adultos y ancianos que existen en su zona." "Las categorías se determinar de acuerdo a la siguiente tabla:"
"CATEGORIA: niños, jovenes, adultos, ancianos" "EDAD: 0-12, 13-29, 30-59, 60-en adelante"    

pesoNiños=0
pesoJovenes=0
pesoAdultos=0
pesoAncianos=0

contadorNiños=0
contadorJovenes=0
contadorAdultos=0
contadorAncianos=0

for i in range (50):
    edad=int (input(f"ingrese la edad de las persona {i+1}: "))
    peso=int  (input(f"ingrese el peso de las persona {i+1}: "))

    if edad <=12:
            pesoNiños+=peso 
            contadorNiños+=1
    elif edad <=29:
            pesoJovenes+=peso
            contadorJovenes+=1
    elif edad <=59:
            pesoAdultos+=peso
            contadorAdultos+=1
    else:
            pesoAncianos+=peso
            contadorAncianos+=1   

promedioN= pesoNiños/contadorNiños 
promedioJ= pesoJovenes/ contadorJovenes 
promedioA= pesoAdultos/ contadorAdultos 
promedioA= pesoAncianos/contadorAncianos

print(f"promedio peso niños es: {promedioN} Kg")
print(f"promedio peso jovenes es: {promedioJ} Kg")
print(f"promedio peso Adultos es: {promedioA} Kg")
print(f"promedio peso Ancianos es: {promedioA} Kg")



    
