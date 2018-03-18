
def f(p):
    print p
    return p

def loop(x):
    while True:
        x += 1
        if x % 10 == 0:
            print "break"
            return None
    return 0

# (f(1), f(3), f(3)) < (f(1), f(2), loop(0))
# [f(1), f(3), f(3)] < [f(1), f(2), loop(0)]
# {1: f(1), 2: f(3), 3: f(3)} < {1: f(1), 2: f(2), 3: loop(0)}

# f(1) < f(2) < f(1) < loop(0)

print [f(1), [f(2), f(3)]] < [f(1), [f(3), loop(0)]]