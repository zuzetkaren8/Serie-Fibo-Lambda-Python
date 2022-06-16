# -*- coding: utf-8 -*-
"""
Created on Tue Jun 14 01:41:45 2022

@author: Zuzet Sanga
"""

from functools import reduce
  
fib = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]+x[-3]],
                                 range(n-3), [0, 1, 1])
n = input()
cant = int(n)  
print(fib(cant))