import random, time
import numpy as np
prev=[]*10
curr=[]*10
while 1:
  prev =[random.randint(0,4)]*10
  print (prev)
  time.sleep(0.5)
  curr=[random.randint(0,4)]*10
  print(curr)
  time.sleep(0.5)
  if (prev > curr):
    prev=[0]*10
    print("prev di reset")
  diff=np.subtract(curr, prev)
  print ("beda",diff)

