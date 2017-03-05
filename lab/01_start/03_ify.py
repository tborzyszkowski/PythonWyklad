aa = [None, {}, {'q': 12}]
bb = [None, "", "Ala"]

str_format2 = '{:^15} {:^15} {:^20} {:^25} {:^30} {:^20}'
print str_format2.format("a", "b",
            "a if a>b else b",
            "(a > b and [a] or [b])[0]",
            "(a > b and {0: a} or {0: b})[0]",
            "a > b and a or b")

# (a > b ? a : b)

for a in aa:
    for b in bb:
        print str_format2.format(a, b
                                , a if a > b else b
                                , (a > b and [a] or [b])[0]
                                , (a > b and {0: a} or {0: b})[0]
                                , a > b and a or b)
