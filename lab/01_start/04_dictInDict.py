d1 = {'a1': 1}
d2 = {'a2': 11, 'b2': d1}
d3 = {'a3': 21, 'b3': d1, 'c3': d2}

print d1
print d2
print d3

print d3['c3']['b2']['a1']
