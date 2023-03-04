import re

# if re.compile("a[b-c]a").match("aba"):
#     print "OK"
# print re.compile("a[b-c]*a").findall("xxxabayyyacaqqqqqqqqqqaaaa")

s = '<html><head><title>Title</title>'
print(re.match('<.*>', s).group())
print(re.match('<.*?>', s).group())

qq = 'ababababababaa'
print(re.match('.*a{2,3}?', qq).group())
