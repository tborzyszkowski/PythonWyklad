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

d = D()

print len(d), d
d['ala'] = 321
print len(d), d
d['ola'] = 123
print len(d), d
print d['ala'], d['ola']
print d.dane.keys()
