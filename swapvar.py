import time

a=23
b=32

#noted
#The classic way to fo it with a temporary variable
#so, let's see

temp=a
a=b
b=temp
print ("a= "+str(a))
print ("b= "+str(b))
#why python is great?
#So, let's see what can python handle this swap.
#Python use this short hand
time.sleep(3)
print "We will demonscrate how python's swaping"
a,b=b,a #Well done
print a
print b
