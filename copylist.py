import random, timeit, time
import numpy as np

sensor=[]
save3=[]
save4=[]
for i in range (10):
    i=random.randint(0,4)
    sensor.extend([i])
time.sleep(1)
save1=sensor[:]
save2=list(sensor)
[save3.append(sensor[item]) for item in range(10)]
[save4.extend([item]) for item in sensor]
print(sensor)
print(save1)
print(save2)
print(save3)
print(save4)
print(id(sensor))
print(id(save1))
print(id(save2))
print(id(save3))
print(id(save4))
print(timeit.timeit(str(save1),number=10000))
print(timeit.timeit(str(save2),number=10000))
print(timeit.timeit(str(save3),number=10000))
print(timeit.timeit(str(save4),number=10000))
# print(np.subtract(sensor,save1))
