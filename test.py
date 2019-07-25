import numpy as np

a = np.array([ i for i in range(50)])
print(a)
l = a.reshape(2,5,5)

print(l)
print()
print(l[1,:,2])
