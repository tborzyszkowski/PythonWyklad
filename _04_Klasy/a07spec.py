# metody specjalne

# obiekt z dlugoscia

class D:
    def __init__(self):
        self.dane = {}
    def __len__(self):
        return 2 * len(self.dane)
    def __getitem__(self, key):
        return self.dane[key]
    def __setitem__(self, key, item):
        self.dane[key] = item
    def __repr__(self):
        return ' '.join(['D: ', repr(self.dane)])
    def __lt__(self, other):
        return len(self) < len(other)

d = D()

print len(d), d
d['ala'] = 321
d['ala'] = (1, 2)
print len(d['ala'])
print len(d), d
d['ola'] = 123
print len(d), d
print d['ala'], d['ola']
print d.dane.keys()

c = D()
print c < d
