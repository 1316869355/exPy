# -*- coding: utf-8 -*-
num = 0
tot = 0.0

while True:
    numInStr = input('please put in a num ')
    print(numInStr)
    if 'Done' == numInStr:
        break
    try:
        numIn = float(numInStr)
        num = num +1
        tot = tot + numIn
    except:
        print('this input not a num ', numInStr)

num = num + numInStr
print('all input num is ', num, ' total:',tot, ' the average:', tot/num)
