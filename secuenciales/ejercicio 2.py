""""
Ejercicio 2
Construya un algoritmo que calcule el perímetro y el área de un rectángulo dada su base y su altura.
La base y la altura deberán ser almacenadas previamente en dos variables respectivamente. El
algoritmo debe mostrar en pantalla el siguiente mensaje: El perímetro del rectángulo es: xxx el área
del rectángulo es: yyyy
"""
#definimos variables por medio de input 
base  =  float ( input ( "Ingrese la base del rectangulo: " )) 
altura  =  float ( input ( "Ingrese la altura del rectangulo: " )) 
#definimos variables que contienen las formulas para hallar perimetro y area
perimetro  =  float ( 2  *  base  +  altura ) 
area  =  float ( base  *  altura ) 
#mandamos a imprimir el mensaje 
print ( " El perimetro del rectangulo es: " , perimetro , ' \n ' , "El area del rectangulo " , area )
