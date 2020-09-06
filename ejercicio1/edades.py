# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""
import time

def calcular_edad(edad, anio_actual):
    print("          ----Bienvenido----")
    print("------Calcula tu edad en el 2070---------")
    anio_tope=2070
    print("")
    if anio_actual and edad>0:
        if anio_actual<=anio_tope:
            print("Calculando...")
            time.sleep(1.0)
            print("")
            edad_2=anio_tope-anio_actual
            edad_final=edad+edad_2
            return edad_final
            print("Su edad en el año 2070 sera: ", edad_final)
        else:
            print("El año actual ingresado es mayor 2070")
    else: 
        print("Error los numeros deben ser mayores a 0")
