a = 100000
b = 12345

def algor(a,b):
    while b != 0:
        c = a % b
        a = b
        b = c
    return a

print (algor(a,b))
