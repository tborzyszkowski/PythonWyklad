osoby = [{'nazwisko': 'Nowak', 'waga': 70,
         'ulubione_dania': ['schabowy', 'pomidorowa']},
         {'nazwisko': 'Kos',   'waga': 30,
         'ulubione_dania': ['lody', 'ciastka']},
         {'nazwisko': 'Szpak', 'waga': 40,
         'ulubione_dania': ['ryz', 'ogorkowa']},
         {'nazwisko': 'Kowalski', 'waga': 70,
         'ulubione_dania': ['schabowy', 'pomidorowa']},
         {'nazwisko': 'Konstantynopolitanczykiewicz', 'waga': 80,
         'ulubione_dania': ['frytki', 'ryba']},
         ]

print "\n".join(["\n{nazwisko}\n{waga}\n{ulubione_dania}".format(**o) for o in osoby])
print [o['nazwisko'] for o in osoby]

osoby.sort(key=lambda o: o['nazwisko'])
print [o['nazwisko'] for o in osoby]

osoby.sort(key=lambda o: o['waga'])
print [o['nazwisko'] for o in osoby]

osoby.sort(key=lambda o: o['ulubione_dania'][0], reverse=True)
print [o['nazwisko'] for o in osoby]

print sorted(osoby, key=lambda o: o['ulubione_dania'][0], reverse=True)

print sorted(osoby,
             cmp=lambda x, y: 1 if x < y else -1,
             key=lambda o: o['ulubione_dania'][0], reverse=True)

print [o['nazwisko'] for o in sorted(osoby,
                                     cmp=lambda x, y: cmp(x[::-1], y[::-1]),
                                     key=lambda o: o['nazwisko'])]

print [o['nazwisko'] for o in sorted(osoby,
                                     key=lambda o:o['nazwisko'].count('a'),
                                     reverse=True)]
