import re

# p = re.compile(r'\W+')
# print p.split('This is a test, short and sweet, of split().')
#
# print p.split('This is a test, short and sweet, of split().', 3)
# #
# print p.split('This... is a test.')
# p2 = re.compile(r'(\W+)')
# print p2.split('This... is a test.')
#
# print re.split('[\W]+', 'Words, words, words.')
# print re.split('([\W]+)', 'Words, words, words.')
# print re.split('[\W]+', 'Words, words, words.', 1)
#
# # ########
#
p = re.compile('(blue|white|red)')
print p.sub('colour', 'blue socks and red shoes')
print p.sub('colour', 'blue socks and red shoes', count=1)
print p.subn('colour', 'blue socks and red shoes')
print p.subn('colour', 'no colours at all')[1]
#
# p = re.compile('x+')
# print p.sub('-', 'abxxxxxxd')
# #
# # # Argumentem sub() moze byc funkcja,
# # # ktora bedzie wywolana na kazdym dopasowaniu wzorca
#
#
# def hexrepl(match):
#     "Return the hex string for a decimal number"
#     value = int(match.group())
#     return hex(value)
#
# p = re.compile(r'\d+')
# print p.sub(hexrepl, 'Call 65490 for printing, 49152 for user code 15 16 14 15.')
# p = re.compile(r'^(a+)+$')
# m = p.match("a"*30+"!")
# if m:
#     print m.span()
# else:
#     print "---"