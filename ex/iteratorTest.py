# -*- encoding: utf-8 -*-

import random

arrToSort = []
for i in range(0, 6):
    print (i)
    num = random.random()
    arrToSort.append(int(num*100))

indx=0
arrToSort.sort(reverse=True)
for j in arrToSort:
    print ("arrToSort index", indx, ": ", j)
    indx += 1
