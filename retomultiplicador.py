# -*- coding: UTF-8 -*-
# 👆 Sin lo de arriba no se puede poner emojis

import random

intrucciones = '''
================= Reto Multiplicador ================

Tienes 3 Vidas y 10 Preguntas de Multiplicación que responder.

Si llegas al final, viene un regalo Especial

=====================================================

'''

def desafio_multuplicador(nombre, pregunta, vidas):
    valor_1= random.randint(2,5)
    valor_2= random.randint(2,5)
    resultado_verdadero = valor_1 * valor_2
    resultado_elegido = int(input('Pregunta {}: Te pregunto, {}. ¿Cuanto es {} por {}? : '.format(pregunta, nombre, valor_1, valor_2)))
    if resultado_elegido == resultado_verdadero:
        print('Excelente! (Aplausos 👏👏👏)')
        return vidas
    else:
        vidas -= 1
        print('Lo siento, el valor verdadero es : {}'.format(resultado_verdadero))
        print('Te quedan {} Vidas '.format(vidas))
        return vidas

def run():
    nombre = (input('Hola Hijo, ¿Cual es tu nombre?: ')).capitalize()
    print('#' * 50)
    print('Bienvenido {} al Juego Multiplicador! (Aplausos 👏)'.format(nombre))
    print('#' * 50)
    print(intrucciones)
    vidas = 3
    pregunta = 1
    while pregunta < 11:
        if vidas > 0:
            vidas = desafio_multuplicador(nombre, pregunta, vidas)
            pregunta += 1
        else:
            print('#' * 50)
            print('Oh, Lo siento, perdiste esta vez, vuelve a intentarlo en la próxima')
            print('#' * 50)
            break
    else:
        print('#' * 50)
        print('Haz Ganado {} (Aplausos 👏), espera tu regalo'.format(nombre))
        print('#' * 50)

if __name__ == '__main__':
    run()