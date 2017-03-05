aList = [{}, {'q': 12}]
bList = ["", "Ala"]
cList = [0, 10]

# w = a and b or c

# str_format = '%10s %10s %10s %10s'
str_format2 = '{:^10} {:^10} {:^10} {:^15} {:^15} {:^15}'
# print str_format % ("a", "b", "c", "a and b or c","(a and b) or c","a and (b or c)")
print str_format2.format("a", "b", "c", "a and b or c","(a and b) or c","a and (b or c)")
for a in aList:
    for b in bList:
        for c in cList:
            # print str_format % (a, b, c, a and b or c)
            print str_format2.format(a, b, c, a and b or c, (a and b) or c, a and (b or c))
