# -*- coding: utf-8 -*-
import math 
"""
Created on Sat Mar 30 10:56:23 2019

@author: Michael
"""
'''================================EXERCICIO==============================='''
'''=========== CALCULADORA ================='''
''' 1'''
x = 10 % 3
print(x)
'''2 '''
for i in range(0,11):
    print("13 x {} = {}".format(i,13*i))
'''3'''
aulasPorsemana = 2
mesesDeaula = 4
semanasNoMes = 4
presencObrig = 75/100

qtdAulas = aulasPorsemana * semanasNoMes * mesesDeaula
minPresenca = qtdAulas * presencObrig
print("Total de aulas: {}, Minino de Presenca: {}, Faltas Permitidas: {}".format(qtdAulas,minPresenca,qtdAulas-minPresenca))
'''4'''
def AreaDoRaio(raio):    
    area = math.pow(raio,2)*math.pi
    return area
r=2
print("Area de do raio de {} é {}".format(r,AreaDoRaio(r)))

'''=======================EXPRESSOES NUMERICAS================'''

'''1'''
horas = 3
minutos = 23
segundos = 17
tempoInicial = str(horas)+":"+str(minutos)+":"+str(segundos)
minutos +=(horas * 60)
segundos +=(minutos*60)
print("{} tem o total de: {} segundos.".format(tempoInicial,segundos))
'''2'''
distancia = 65 #em Km
distancia *= 1000 # transormando em metros
velMedia = distancia /segundos
print("Velocidade media de {}m/s".format(round(velMedia,2)))
'''3==================================================================='''
exp = (100 - 413 * (20 - 5 * 4))/ 5
print(exp)
'''4==================================================================='''
c = [0,0,0]
for z in range(0,3):
    c[z] =float(input('Informe o valor do {}º capacitor'.format(z+1)))
x=input('[1]- Serie / [2]-Paralelo')
x =int(x)
soma = 0
if x==2:
    for i in range(0,3):
        soma += c[i]
    print("Capacitancia resultante é {}".format(round(soma,2)))
else:
    for i in range(0,3):
        soma += 1/c[i]
    cp = 1/soma
    print("Capacitancia resultante é {}".format(round(cp,2)))