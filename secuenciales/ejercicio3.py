""""
Elabore un algoritmo que calcule el promedio de tres números, los cuales deben ser almacenados
previamente en tres variables. El algoritmo debe imprimir el siguiente mensaje: El promedio de los
números ingresado es: xxxx
"""
numero1 = int(input("ingrese el primer numero:")) # definimos la primer variable 
numero2 = int(input("ingrese el segundo numero:")) #definimos la segunda variable 
numero3 = int(input("ingrese el tercer numero:")) #definimos la tercera variable 
suma = int(numero1 + numero2 + numero3 ) #definimos la variable con la suma  
promedio = int(suma / 3) #definimos la variable con la definicion 
print("el promedio de los numero es: ",promedio )#mandamos a imprimir el mensaje 