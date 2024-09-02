" Escribir un programa que multiplique los 20 primeros números naturales. Ejemplo: (1*2*3*4*5…)"

# Inicializar producto
producto = 1
# Multiplicar los 20 primeros números naturales
for i in range(1, 21):
 producto *= i
# Imprimir el resultado
print(f"El producto de los 20 primeros números naturales es: {producto}")
