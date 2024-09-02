"Leer 10 números negativos y convertirlos a positivos e imprimir la suma de dichos números"
#se agrega el contador
numerosPositivos=0
for a in range (10):
    numero=int(input(f"ingresa el numero negativo {a+1}:"))
    if numero < 0:
        #se convierten a positivos
        numerosPositivos +=abs(numero)
#se imprimen los numeros negativos a positivos 
print(f"esta es la suma de numeros negativos convertidas a numeros positivos = {numerosPositivos}")
    


