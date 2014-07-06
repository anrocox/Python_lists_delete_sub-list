#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 3, 2014

@author: anroco

How to remove a sublist in python?

¿Como eliminar una sublista en python?
'''

#create a list
lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
print (lista)

#use del statement to remove a slice of the list.
del lista[1:5]
print(lista)

#remove slices using negative indices.
del lista[-4:-1]
print(lista)
