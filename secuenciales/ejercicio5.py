"""
Desarrolle un algoritmo de Programa que calcula el precio final de una compra, dado el valor de la
compra y un descuento. Para esto es necesario declarar dos variables, una que guarde el valor de la
compra y otra que almacene el valor del descuento. El algoritmo debe mostrarse en pantalla, el valor.
de la compra el valor del descuento y el valor final a pagar.
Ejemplo:
La compra fue xxxx, con un descuento de yyyy y el valor final a pagar es zzzz
"""
#Definimos variables
valorCompra  =  float ( input ( "Ingrese el valor de la compra: " )) #ingresamos el valor de la compra
descuento  =  float ( input ( "Ingrese el valor del descuento (como porcentaje): " )) #Pedimos que ingresen la cantidad de descuento

# hacemos la operacion del descuento en dinero
montoDescuento  =  valorCompra  * ( descuento  /  100 )

# se calcula el valor final 
valorFinal  =  valorCompra  -  montoDescuento

# resultado final 
print ( "La compra fue" , valorCompra , "con un descuento de" , descuento , "y el valor a pagar es" , valorFinal )