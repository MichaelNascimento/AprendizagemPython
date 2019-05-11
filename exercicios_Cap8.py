# -*- coding: utf-8 -*-
"""
Created on Sat May 11 13:06:33 2019

@author: Michael
"""

frase = input("Informe uma frase: \n");
palavra1 = frase.split();

for i in palavra1:
    print("{} , {}".format(i,len(i)));
    
print('\nA frase "{}" tem {} caracteres'.format(frase,len(frase)));

print('\n Frase {} ao contrario é {}'.format(frase,frase[::-1]));