q, w, e, r = 1, 2, 3, 4
print(q+r); print(w*r); print(r/w); print(e*r)



a= "Hello"
s= " World!"
print(a+s)

import random
list = [11, 22, 33, 44, 55, 66, 77, 88, 99, 00]
print ("random.sample() ", random.sample(list,9))

random.sample(range(10), 10)
a=[random.randint(0,50) for i in range(10)]
print(a.pop())
print(a)