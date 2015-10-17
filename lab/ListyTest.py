import copy
l = [1, 'aaa', {1:[0]}]
qq = copy.deepcopy(l)
ll = l *2
ll[2][1].append(1)
l[2][1].append(2)
print l
print ll
print qq

l = (1, 'aaa', {1:[0]})
ll = l *2
ll[2][1].append(1)
print l
print ll