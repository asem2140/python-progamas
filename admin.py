import csv
from correo import *

#Encabezado de la entrada de datos
print("\n\n*******************************************************")
print("           DATOS DE POTENCIALES CLIENTES")
print("*******************************************************")

aceptados = 0
rechazados = 0

with open('encuesta.csv') as encuesta:
    csv_reader = csv.reader(encuesta, delimiter=',')

    for row in csv_reader:
        print(f'* {row[0]}:\n') #f permite incrustar variables en cadena de caracteres, para ello, envolver en llaves la variable
        print(f'\t- Correo: {row[1]}')
        print(f'\t- ¿Toma bebidas hidratantes?: {row[2]}')
        print(f'\t- ¿Qué marca de bebida consume?: {row[3]}')
        print(f'\t- ¿Considera que se hidrata adecuadamente?: {row[4]}')
        print(f'\t- ¿Cuánto paga por una bebida hidratante?: {row[5]}')
        print(f'\t- ¿Con qué frecuencia se hidrata cuando hace ejercicio?: {row[6]}')
        print(f'\t- ¿Cuánto gasta en productos hidratantes mensualmente?: {row[7]}')
        print(f'\t- Aproximadamente, ¿cúantos litros de agua consume al día?: {row[8]}')        
        print(f'\t- Fecha en que se realizó la encuesta: {row[9]}')
        print('\n¿Debe ser considerado para el plan de marketing?')
        decision = input()
        if decision.lower() == 'si':
            correo = Correo(row[1])
            correo.enviarEmail()
            aceptados += 1
        else:
            print(f'{row[0]} ha sido descartado del plan de marketing.\n')
            rechazados += 1

print('\n******** RESULTADOS ********\n')
print(f'N° de personas aprobadas: {aceptados}\n')
print(f'N° de personas rechazadas: {rechazados}\n')
