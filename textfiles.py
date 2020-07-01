# -*- coding: utf-8 -*-
"""
Created on Thu Dec 20 23:46:54 2018

@author: Shrikant
"""

with open("c:/PyCodes/test.txt",'w',encoding = 'utf-8') as f:
   f.write("my first file\n")
   f.write("This file\n")
   f.write("contains three lines\n")
   print("Writing file .... Done")
   
with open("c:/PyCodes/test.txt",'r',encoding = 'utf-8') as f:  
   print(f.read(8))
   print("Reading file .... Done")

with open("c:/PyCodes/test.txt",'r',encoding = 'utf-8') as f:     
   for line in f:
       print(line, end = ' ')

with open("c:/PyCodes/test.txt",'r',encoding = 'utf-8') as f:     
   print(f.readline())
with open("c:/PyCodes/test.txt",'r',encoding = 'utf-8') as f:     
   for line in f:
       print(f.readline())
       print(f.readline())
       print(f.readline())
      
       
f = open('c:/PyCodes/test.dat', 'w+b')
byte_arr = [120, 3, 255, 0, 100]
binary_format = bytearray(byte_arr)
f.write(binary_format)
f.write(binary_format)
f.close()

f = open('c:/PyCodes/test.dat', 'r+b')
bnft=f.read(4)
xx=list(bnft)
print(xx)
bnft2=f.read()
yy=list(bnft2)
print(yy)
f.close()
