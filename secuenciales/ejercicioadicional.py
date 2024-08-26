""""
Desarrolle un algoritmo que permita calcular nota final de algoritmia de un estudiante dadas las
siguientes apreciaciones:
• Las actividades en clase equivalen a un porcentaje de 30%.
• Proyecto final 50%
• Evaluaciones parciales 20%
Para esto es importante definir 4 variables.
Variable 1 que almacene el nombre del estudiante
Variable 2 que almacena la calificación promedio de las actividades realizadas en clase
Variable 3 que almacene la calificación del proyecto final
Variable 4 que almacene la calificación promedio de las evaluaciones parciales
Se debe calcular la calificación final.
El algoritmo debe mostrar el nombre del estudiante, junto con la nota final del estudiante.
Ejemplo: La nota final de algoritmia del estudiante xxxx es: yyyy
"""
# Definir las variables
nombreEstudiante  =  input ( "Ingrese el nombre del estudiante: " ) #se ingresa el nombre del estudiante 
calificacionActividades  =  float ( input ( "Ingrese la calificación promedio de las actividades en clase (0-100): " )) #imgresamos la calificacion de las actividades
calificacionProyecto  =  float ( input ( "Ingrese la calificación del proyecto final (0-100): " )) #ingresamos la calificacion final del proyecto
calificacionEvaluaciones  =  float ( input ( "Ingrese la calificación promedio de las evaluaciones parciales (0-100): " )) #ingresamos el promedio de las evaluaciones 

# Definir los porcentajes
porcentajeActividades  =  0.30
porcentajeProyecto  =  0.50
porcentajeEvaluaciones  =  0.20

# Calcular la nota final
notaFinal  = ( calificacionActividades  *  porcentajeActividades  +
              calificacionProyecto  *  porcentajeProyecto  +
              calificacionEvaluaciones  *  porcentajeEvaluaciones )

#Imprimimos el resultado
print ( "La nota final de algoritmia del estudiante" , nombreEstudiante , "es:" , round ( notaFinal , 2 )) #funcion "round " para redondear un número decimal largo
