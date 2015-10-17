import re

phonePattern = re.compile(r'''
                # don't match beginning of string, number can start anywhere
    (\d{3})     # area code is 3 digits (e.g. '800')
    \D*         # optional separator is any number of non-digits
    (\d{3})     # trunk is 3 digits (e.g. '555')
    \D*         # optional separator
    (\d{4})     # rest of number is 4 digits (e.g. '1212')
    \D*         # optional separator
    (\d*)       # extension is optional and can be any number of digits
    $           # end of string
    ''', re.VERBOSE)

print phonePattern.search('work 1-(800) 555.1212 #1234').groups()
print phonePattern.search('work 1-(800) 555.1212 #1234').group()
print phonePattern.search('800-555-1212').groups()
print phonePattern.search('800-555-1212').group()


# ###############################

m = re.compile("(a(b)c)d").match("abcd")
print m.groups()
print m.group(0), m.group(1), m.group(2)
print m.group(2, 1, 2)

p = re.compile(r'(\b\w+)\s+\1')
print p.search('Paris in the the spring').group()

# Wyjasnienia
#   \b tylko pelne slowa
#   \1 w tym miejscu dopasowanie grupy o numerze 1