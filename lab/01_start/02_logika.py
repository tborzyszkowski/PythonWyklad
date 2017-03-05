a = [{}, {'q': 12}]
b = ["", "Ala"]
c = [0, 10]

# w = a and b or c

# str_format = '%10s %10s %10s %10s'
str_format2 = '{:^10} {:^10} {:^10} {:^10}'
# print str_format % ("a", "b", "c", "a and b or c")
print str_format2.format("a", "b", "c", "a and b or c")
for aa in a:
    for bb in b:
        for cc in c:
            # print str_format % (aa, bb, cc, aa and bb or cc)
            print str_format2.format(aa, bb, cc, aa and bb or cc)
