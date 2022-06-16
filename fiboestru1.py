# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 01:48:11 2022

@author: Zuzet Sanga
"""

def fibonacci(count):
   listA = [0, 1, 1]

   any(map(lambda _:listA.append(sum(listA[-3:])),
         range(3, count)))

   return listA[:count]
n = input()
cant = int(n)
print(fibonacci(cant))