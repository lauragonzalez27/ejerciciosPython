"La oficina de tránsito de Ibagué desea saber, de los n autos que entran a la ciudad de Ibagué,"
"cuantos entran con calcomanía de cada color. Conociendo el ultimo dígito de la placa de cada carro," 
"se puede determinar el color de la calcomanía utilizando la siguiente relación:"
"DIGITO  1 o 2, 3 o 4, 5 o 6, 7 o 8, 9 o 0"        "COLOR amarillo, rosa, rojo, verde, azul"

# Inicializar contadores para cada color
contadorRojo = 0
contadorVerde = 0
contadorAmarillo = 0
contadorAzul = 0
contadorRosa = 0

# Leer la cantidad de autos
n = int(input("Ingrese la cantidad de autos que entran a Ibagué: "))

# Leer el último dígito de la placa de cada auto
for i in range(n):
    ultimoDigito = int(input(f"Ingrese el último dígito de la placa del auto {i+1}: "))
    
    # Determinar el color de la calcomanía basado en el último dígito
    if ultimoDigito == 1 or ultimoDigito == 2:
        contadorAmarillo += 1
    elif ultimoDigito == 3 or ultimoDigito == 4:
        contadorRosa += 1
    elif ultimoDigito == 5 or ultimoDigito == 6:
        contadorRojo += 1
    elif ultimoDigito == 7 or ultimoDigito == 8:
        contadorVerde += 1
    elif ultimoDigito == 9 or ultimoDigito == 0:
        contadorAzul += 1
    else:
        print("Color no determinado")  # En caso de que se ingrese un número fuera del rango (0-9)

# Imprimir los resultados
print(f"Autos con calcomanía amarilla: {contadorAmarillo}")
print(f"Autos con calcomanía rosa: {contadorRosa}")
print(f"Autos con calcomanía roja: {contadorRojo}")
print(f"Autos con calcomanía verde: {contadorVerde}")
print(f"Autos con calcomanía azul: {contadorAzul}")