# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 13:01:19 2019

@author: Michael
"""

'''#from __future__ import division'''
 

'''criando funções'''
def another_double(x):
    return 2 * x

var = 5

another_double(var) # chamando a função another_double

print (var) # imprimindo na tela o valor de x


#---------------------------------------------------------------------
'''Criando função com parametro padrao '''

def my_print(msg="minha mensagem padrão"):
    print (msg)

my_print("teste") # chaando a funçao mas mandando um argumento

my_print() # chmanado a função sem argumento


def subtrair(a=0, b=0):
    return a - b

print(subtrair(10,5))
print(subtrair())
print(subtrair(b=5))

#---------------------------------------------------------------------------
'''Exceções'''
try:
    print(0 / 0)
except ZeroDivisionError:
    print ("Não é possivel divisão por 0")
    
#--------------------------------------------------------------------------
'''Listas'''

lista_de_inteiros = [1,2,3]
lista_varios_tipos = ["String", 0.2, True]
lista_de_lista = [lista_de_inteiros,lista_varios_tipos, []]

print("tamanho da lista")
print(len(lista_de_inteiros)) # imprime a qtd de itens da lista
print("soma da lista")
print (sum(lista_de_inteiros)) #imprime a soma dos itens da lista

x = range(10)
print("ultimo valor da lista")
print (x[-1]) # imprimindo o ultimo item da lista

if 10 in x:
    print("true")
else:
    print("false")

x,y = [1,2]

print(x) # imprime 1
print(y) # imprime 2

#--------------------------------------------------------------------------------------
'''Tuplas'''

my_list = [1,2]
my_tuple = (1,2)
other_tuple = 3,4
my_list[1] = 3
try:
    my_tuple[1] = 3
except:
    print("Não é possivel modificar uma tupla")

def soma_e_produto(x,y):
    return (x + y),(x * y)

sp = soma_e_produto(3,5)
soma,produto = soma_e_produto(2,7)
print('sp = {sp}, soma = {soma}, produto = {produto}'.format(sp = sp,soma=soma, produto=produto)) # sp = (8, 15), soma 
print(x,y)
x,y = y,x # trocando de valores
print(x,y)

#----------------------------------------------------------------------------------------------
'''Dicionarios'''

empty_dict =  {}
empty_dict2 = dict()
grades = {"Joel": 80, "Tim": 95}
joels_grades = grades["Joel"] # é igual a 80
print(joels_grades)
try:
    kates_grades = grades["Kate"]
except:
    print("Se notas para kate")
    
joel_has_grades = "Joel" in grades # True Joel existe em grades
kate_has_grades = "Kate" in grades # falso kate não existe em grades

print('grades existe: Joel = {}, Kate = {} '.format(joel_has_grades,kate_has_grades))
joel_grades = grades.get("Joel",0) # 80
kate_grades = grades.get("Kate",0) # 0

#Substituindo valores
grades["Tim"] = 99 # substitui o valor antigo por 99
num_students = len(grades)
print(num_students)  # imprime 2
grades["kate"] = 100 # adiciona se não existir
num_students = len(grades)
print(num_students) # imprime 3

tweet = {
        "user" : "Thais Deodoro",
        "text" : "Enfermagem Neonatal",
        "retweet_count" : 100,
        "hastags" : ["#data","#science","datascience","awesome","yolo"]
        }

tweet_keys = tweet.keys()
tweet_values = tweet.values()
tweet_itens= tweet.items()
print(tweet_itens)

#----------------------------------------------------------------------------------------
'''defaultDict'''
