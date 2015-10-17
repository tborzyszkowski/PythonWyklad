
d = {'a':1, 'b':2, 'c':3}
for k in d:
    print k, d[k]
    
    
# switch statement
 
def zero():
    print "You typed zero.\n"
 
def sqr():
    print "n is a perfect square\n"
 
def even():
    print "n is an even number\n"
 
def prime():
    print "n is a prime number\n"
    
options = {0 : zero,
           1 : sqr,
           4 : sqr,
           9 : sqr,
           2 : even,
           3 : prime,
           5 : prime,
           7 : prime,
           }

num = 5
options[num]()