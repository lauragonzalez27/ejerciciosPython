"Suponga que se tiene un conjunto de calificaciones de un grupo de 20 alumnos." 
"Realizar un algoritmo para calcular el promedio y la calificación más alta y más baja de todo el grupo."

calificacionAlta=5
calificacionBaja=0
promedio=0
suma=0

for i in range (20):
    numero=int(input(f"ingrese la calificacion {i+1}:"))
    suma=numero 
    if suma> calificacionAlta:
        calificacionAlta= suma 
        
    if suma< calificacionBaja:
        calificacionBaja= suma 


promedio= suma/20
print (f"calificacio alta {calificacionAlta}") 
print (f"calificacion baja {calificacionBaja}")
print (f"promedio es {promedio}" )
        




