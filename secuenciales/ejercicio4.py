""""
Construya un algoritmo que calcula el sueldo total de un vendedor, dado su sueldo base y las
comisiones de sus ventas. Para esto es necesario definir una variable que almacene el nombre del
vendedor, una variable que almacene el sueldo y otra variable que almacene el valor de la comisión
de las ventas realizadas. Se debe calcular el valor final de sueldo. El algoritmo debe imprimir el
nombre del vendedor, el valor del sueldo, el valor de su comisión y el sueldo total del vendedor.
Ejemplo: El vendedor Pepito Pérez, tiene un sueldo de xxxx, durante el mes obtuvo una comisión de
yyyy y el valor final a pagar es: zzzz
"""
#Definimos variables
nombreVendedor  =  input ( "Ingrese el nombre del vendedor: " ) #se ingresa la variable del nombre del vendedor
sueldoBase  =  float ( input ( "Ingrese su sueldo base: " )) #se ingresa la variable del sueldo base
ventas  =  int ( input ( "Ingrese el numero de ventas mensuales: " )) #se ingresa las ventas que realizo mensuales
comisionVenta  =  float ( 5000 ) #Definimos la variable del valor de la comisión por venta
sueldoComision  =  float ( ventas  *  comisionVenta ) #calculamos la operacion de comisión por el número de ventas mensuales con la variable sueldoMasComision
sueldoTotal  =  sueldoBase  +  sueldoComision #Definimos la variable "SueldoTotal" realizando la suma del sueldo base mas la comision
#Mandamos a imprimir el mensaje concatenando las variables
print ( " El vendedor " , nombreVendedor , ", tiene un sueldo de " , sueldoBase , " pesos " , ", durante el mes obtuvo una comisión de " , sueldoComision , " y el valor final a pagar es: " , sueldoTotal )
