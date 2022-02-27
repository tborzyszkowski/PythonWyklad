import math

samples = [((1, 2, 1), {'wynik': 1, 'x1': -1, 'x2': None}),
           ((1, 0 , 1), {'wynik': 0, 'x1': None, 'x2': None}),
           ((1, -5 , 6), {'wynik': 2, 'x1': 2, 'x2': 3})]

for sample in samples:
    result = {'wynik': None, 'x1': None, 'x2': None}
    a, b, c = sample[0]
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
    if result == sample[1]:
        print(sample, result, "OK")
    else:
        print(sample, result, "NOT OK")