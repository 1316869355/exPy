# -*- coding: utf-8 -*-
import numpy as np
import random 
npL = np.array([[j+int(random.random()*100) for j in range(100,1000,100)] for i in range(10,20)])

print(npL)
print(npL[:,1])
