# -*- coding: utf-8 -*-
"""
Created on Fri Mar 19 14:11:54 2021

@author: Esteban Henao
"""

def factorial(n):
    '''Calcula el factorial de n.
    n int > 0
    returns n!'''
    
    print(n)
    if n==1:
        return 1
    
    return n * factorial(n - 1)

n = int(input("Escribe un numero: "))

print(factorial(n))