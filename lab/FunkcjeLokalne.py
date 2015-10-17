'''
Created on 23-03-2014

@author: Tomasz
'''
def fun_loc(n):
    return n-1

def fun1(n):
    def fun_loc(n):
        return n+1
    
    return fun_loc(n)+1

print fun1(2)