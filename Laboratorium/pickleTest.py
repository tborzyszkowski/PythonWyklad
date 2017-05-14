import pickle 

class A:
    def __init__(self,a):
        self.a = a
    def __repr__(self):
        return "A.a = %s" % str(self.a)
    
z = 1+2j
a = A(z)
print a
s = pickle.dumps(a)
aa = pickle.loads(s)
print '------'
print a is aa, a.a is aa.a
print aa
aa.a = 2+1j  

print aa, a
