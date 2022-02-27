import math

samples = [{'a': 1, 'b': 2, 'c': 1,
            'expected': {'wynik': 1, 'x1': -1, 'x2': None},
            'actual': None
            },
           {'a': 1, 'b': 2, 'c': 1,
            'expected': {'wynik': 1, 'x1': -1, 'x2': None},
            'actual': None
            }
           ]

for sample in samples:
    result = {'wynik': None, 'x1': None, 'x2': None}
    a, b, c = (sample['a'], sample['b'], sample['c'])
    delta = b*b - (4*a*c)
    if delta > 0:
        result['wynik'] = 2
        result['x1'] = (-b - math.sqrt(delta))/2*a
        result['x2'] = (-b + math.sqrt(delta))/2*a
    elif delta == 0:
        result['wynik'] = 1
        result['x1'] = (-b + math.sqrt(delta)) / 2
    else:
        result['wynik'] = 0
    sample['actual'] = result


for sample in samples:
    if sample['expected'] == sample['actual']:
        print(sample, "OK")
    else:
        print(sample, "NOT OK")