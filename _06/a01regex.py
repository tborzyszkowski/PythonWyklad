import re

p = re.compile('ab*')
print p

q = re.compile('ab*', re.IGNORECASE)
print q
