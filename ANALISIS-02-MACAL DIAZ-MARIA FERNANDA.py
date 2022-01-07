
#Mensaje de bienvenida
print("Bienvenid@ a Synergy Logistics")

import csv
import pandas as pd

#AGREGAR COLUMNA CON LA RUTA
#Abrir base original como lectura
with open("synergy_logistics_database.csv","r") as operaciones:
    lector_rutas = csv.reader(operaciones)

    #Abrir nueva base como escritura
    with open ("rutas_database.csv", "w") as imp_exp:
        escritor_rutas = csv.writer(imp_exp) 
        
        #Concatenar país origen & destino y agregar la columna al inicio
        for row in lector_rutas:
            nueva_ruta = ["".join([row[2],"-",row [3]])] + row [0:]
            escritor_rutas.writerow(nueva_ruta)

#VALOR TRANSACCIONES POR MEDIO DE TRANSPORTE
#Definir listas vacias por cada medio de transporte
sea = []
rail = []
air = []
road =[]

with open("rutas_database.csv","r") as imp_exp:
    lector_rutas = csv.DictReader(imp_exp)
#Agregar en las listas vacias por transporte los valores totales de cada transacción
#Dividir los totales por 1,000,000 para simplificar el análisis
    for ruta in lector_rutas:
        if ruta["transport_mode"] == "Sea":
            sea.append(int(ruta["total_value"]))
            total_by_sea = sum(sea)/1000000    
        elif ruta["transport_mode"] == "Rail":
                rail.append(int(ruta["total_value"]))
                total_by_rail = sum(rail)/1000000
        elif ruta["transport_mode"] == "Air":
                air.append(int(ruta["total_value"]))
                total_by_air = sum(air)/1000000
        elif ruta["transport_mode"] == "Road":
                road.append(int(ruta["total_value"]))
                total_by_road = sum(road)/1000000   

print ("Sea total = " )
print (total_by_sea)
print ("Rail total = " )
print (total_by_rail)
print ("Air total = " )
print (total_by_air)
print ("Road total = " )
print (total_by_road)


#VALOR TRANSACCIONES POR PAÍS ORIGEN
#Función calculo suma total para lista de rutas
#def calcular_total():
#   total = 0
#    with open("rutas_database.csv","r") as imp_exp:
#        lector_rutas = csv.reader(imp_exp)
#    for row in lector_rutas:
#        valor = row[10]
#        total += valor
#    total_value = total
#    return total_value

#def analizar_trans():
#    analisis = []
#    with open("rutas_database.csv","r") as imp_exp:
#        lector_rutas = csv.DictReader(imp_exp)
#    for transporte in lector_rutas:
#            sublista_trans = [transporte]
#            total_trans = calcular_total(lector_rutas[transporte])
#            sub_lista.append(f'El valor total de la ruta es: {total_trans}')
#            analisis.append(sub_lista)
#    return analisis

with open("rutas_database.csv","r") as imp_exp:
    lector_rutas = csv.DictReader(imp_exp)
    lista_rutas = list(lector_rutas)
 
def total_país (ruta):
    total_valor = ruta["total_value"]
    país_origen = ruta["origin"]
    total_país = sum(total_valor)/1000000
    print(f"Valores totales en millones de pesos por país origen {país_origen}:{total_país}")

#valores_miles_país = [total_país(lector_rutas)]
#print(valores_miles_país)

total_país(lista_rutas[0])

    


















