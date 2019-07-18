import datetime
import csv
from persona import *

#Obtenemos la fecha y hora actual
fecha = datetime.datetime.now()

#Creamos una instancia de la clase persona
persona1 = Persona()

persona1.fecha = fecha

#Encabezado de la entrada de datos
print("\n\n*******************************************************")
print("           ENCUESTA SOBRE CONSUMO DE BEBIDAS")
print("*******************************************************")

#Lectura de datos por consola
print ("\nIngrese su nombre completo:")
persona1.nombre = input()

print ("\nIngrese su correo electrónico:")
persona1.correo = input()

print ("\n¿Toma bebidas hidratantes?:")
persona1.tomaBeb = input()

print ("\n¿Qué marca de bebida consume?:")
persona1.marcaBeb = input()

print ("\n¿Usted considera que se hidrata adecuadamente?:")
persona1.hidrata = input()

print ("\n¿Cuánto paga por una bebida hidratante?:")
persona1.capacPago = input()

print ("\n¿Con qué frecuencia se hidrata cuando hace ejercicio?:")
persona1.bebEjer = input()

print ("\n¿Cuánto gasta en productos hidratantes mensualmente?:")
persona1.gastoBeb = input()

print ("\nAproximadamente, ¿cúantos litros de agua consume al día?:")
persona1.litBeb = input()

#Escritura de datos en el archivo encuesta.csv
with open('encuesta.csv', mode='a', newline='') as encuesta:
    encuesta = csv.writer(encuesta, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    encuesta.writerow([persona1.nombre, persona1.correo, persona1.tomaBeb, persona1.marcaBeb, persona1.hidrata, persona1.capacPago, persona1.bebEjer, persona1.gastoBeb, persona1.litBeb, persona1.fecha])