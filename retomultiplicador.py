# -*- coding: UTF-8 -*-
# 👆 Sin lo de arriba no se puede poner emojis

import random

def desafio_multuplicador(nombre):
    valor_1= random.randint(1,5)
    valor_2= random.randint(1,5)
    resultado_verdadero = valor_1 * valor_2
    resultado_elegido = int(input('Te pregunto, {}. ¿Cuanto es {} por {}? : '.format(nombre, valor_1, valor_2)))
    if resultado_elegido == resultado_verdadero:
        print('Excelente! (Aplausos 👏👏👏)')
    else:
        print('Lo siento, el valor verdadero es : {}'.format(resultado_verdadero))

def run():
    nombre = (input('Hola Hijo, ¿Cual es tu nombre?: ')).capitalize()
    print('Bienvenido {} al Juego Multiplicador! (Aplausos 👏)'.format(nombre))
    desafio_multuplicador(nombre)
    desafio_multuplicador(nombre)
    desafio_multuplicador(nombre)
    
if __name__ == '__main__':
    run()