import re

if re.compile("a[b-c]a").match("aba"):
    print "OK"
print re.compile("a[b-c]*a").findall("xxxabayyyacaqqqqqqqqqqaaaa")
