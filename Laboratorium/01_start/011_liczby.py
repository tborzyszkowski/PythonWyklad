import time
import math
import sys

if sys.platform == 'win32':
    # On Windows, the best timer is time.clock
    default_timer = time.clock
else:
    # On most other platforms the best timer is time.time
    default_timer = time.time

t0 = default_timer()
x = 12345 ** 123456
t1 = default_timer()
xLen = len(str(x))
t2 = default_timer()

print "Time pow:", t1 - t0, "Time len:", t2 - t1, "Len:", xLen

t0 = default_timer()
x = 12345 ** 123456
t1 = default_timer()
xLen=int(math.ceil(math.log(x,10)))

t2 = default_timer()

print "Time pow:", t1 - t0, "Time len:", t2 - t1, "Len:", xLen


