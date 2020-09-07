# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 00:10:29 2020

@author: Leonardo Quintero P
"""


def tomarpalabra(palabra):
    
    primer_caracter = palabra[0]
    print("El primer caracter es: ", primer_caracter)  
    ultimo_caracter=palabra[len(palabra)-1]
    print("El primer caracter es: ", ultimo_caracter)
    print("El tamaño es: ", len(palabra)) 
    return primer_caracter, ultimo_caracter