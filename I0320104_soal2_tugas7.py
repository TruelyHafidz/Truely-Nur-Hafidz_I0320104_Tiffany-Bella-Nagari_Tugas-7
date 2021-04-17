a = 100.134
b = -78.33
c = -222.9
print("a= ", a)
print("b= ", b)
print("c= ", c)
print('*'*100)

#1. metode abs(x)
print('1. metode abs', '-'*20)
print("|a|= ", abs(a))
print("|b|= ", abs(b))
print("|c|= ", abs(c))
print('\n')

#2.metode ceil
print('2.metode ceil', '-'*20)
import math
print("math a ceil= ", math.ceil(a))
print("math b ceil= ", math.ceil(b))
print("math c ceil= ", math.ceil(c))
print('\n')

#3. metode min max
print('3.metode max min', '-'*20)
print('nilai max= ', max(a,b,c) )
print('nilai min= ', min(a,b,c))
print('\n')

#4metode random
print('4. metode random', '-'*20)
import random
x = [a,b,c]
print('x= ', x)
print("random 1")
print('hasil =', random.choice(x))
print("random 2")
print('hasil =', random.choice(x))
print("random 3")
print('hasil =', random.choice(x))
