# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 11:24:34 2019

@author: Michael
"""

''' Dado 3 valores inteiros lidos do teclado: A, B e C, retorne a soma deles. Porém, caso algum desses valores seja
13, então ele não conta para a soma, e os valores a sua direita também não.
Por exemplo:
                        1, 2, 3 -> 6
                        1, 2, 13 -> 3
                        1, 13, 3 -> 1
                        13, 2, 3 -> 0

'''
num = [0,0,0]
opcao = 1
while opcao == 1:
    soma = 0
    #entrada de dados
    for i in range(0,3):
        num[i] = int(input('Informe um numero para a posicao {}:\t'.format(i+1)))
    #logica  
    for i in range (0,3):
        if num[i] == 13:
            break
        soma += num[i]
    print("soma: {}".format(soma))
    opcao = int(input("Repetir: 1-Sim / 2-Nao"))
print("Fim de programa")

'''Alanderson quer saber se um endereço IP é válido. Faça um programa para ajudar Alanderson a testar se um
endereço é válido.
Para isso, a entrada deve ser um endereço IP (digitado pelo usuário) e o programa deve escrever na tela se é
válido ou não. Um endereço IPv4 é composto por 4 números inteiros entre 0 e 255, separados por um ponto.
Por exemplo, o endereço 123.123.123.123 é válido, mas 666.123.k.3 não é '''
def is_numeric(s):
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

ip = ""
opcao =1
while opcao == 1:
    ip = input("Informe um endereço IP:\t\t")
    ip_valido = False
    ip = ip.split(".")
    for i in range(0,3):
        try:
            octeto = int(ip[i]) 
            if is_numeric(octeto):
                if octeto>=0 and octeto<256:
                    ip_valido = True
                else:
                    ip_valido = False
        except:
            ip_valido = False
            break
        #fim do try
     #fim do for  
    if ip_valido == False:
        print("Ip informado é invalido!")
    else:
        print("Ip informado é valido!")
        opcao = int(input("continuar: 1- Sim\ 2-Nao"))

'''Crie uma função que receba 3 valores e calcula as raízes da fórmula de Bhaskara.'''
'''Dica: raiz quadrada é sqrt(), importando math: math.sqrt()Faça um teste com bhaskara(1, -4, -5) e o programa deve obter as raízes: (5.0, -1.0)'''

import math


def bhaskara(a,b,c):
    aux = math.sqrt(pow(b,2)-4*a*c)
    x=[(-b+aux)/2*a,(-b-aux)/2*a]
    return x

print("Raizes: {}".format(bhaskara(1,-4,-5)))