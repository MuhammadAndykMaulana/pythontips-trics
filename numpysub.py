import random, time
import numpy as np

prev=[]
curr=[]
while 1:
  for i in range (10):
    i=random.randint(0,4)
    prev.extend([i])
  print (prev)
  time.sleep(0.5)
  for i in range (10):
    i=random.randint(0,4)
    curr.extend([i])
  print(curr)
  time.sleep(0.5)
  diff=np.subctract(curr, prev)
  if (prev > curr):
    prev=[0]*10
    print("prev di reset")
    
 
