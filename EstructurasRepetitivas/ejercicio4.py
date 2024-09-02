"Calcular e imprimir la tabla de multiplicar de un número cualquiera, el cual se digitará por teclado."
"Imprimir el multiplicando, el multiplicador y el producto."
#ingresamos el numero a multiplicar 
numero= int(input(f"ingrese el numero para la tabla de multiplicar: "))
#definimos el rango a 11 veces 
for i in range(1,11):
    multiplicador=(numero*i) #utilizando el contador "i" para la escala de la multiplicacion
    print (f"{numero} x {i}= {multiplicador}")
