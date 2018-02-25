import time
import math

t0 = time.time()
x = 12345 ** 678900
y =len(str(x))

print "Time:", time.time() - t0, "Len:", y 

t0 = time.time()
x = 12345 ** 67890
z=math.ceil(math.log(x,10))

print "Time:", time.time() - t0, "Len:", z 


