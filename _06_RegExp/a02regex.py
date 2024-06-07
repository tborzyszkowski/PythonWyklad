import re

# print(re.compile("a").match("ba", 1))
# print(re.compile("^a").match("ba", 1))
# print(re.compile("a*").match("baaaaa", 1).group())
# print(re.compile("a*").match("baaaaa", 1).span())

# re.compile("^a").search("ba", 1).group()
# re.compile("^a").search("ba", 1).span()

# re.compile("^a").search("\na", re.DOTALL).group()
# re.compile("^a").search("\na").span()

# print(re.compile("^a", re.MULTILINE).search("\na", 1).group())
# print(re.compile("^a", re.M).search("\na", 1).span())
#
# re.compile("^a", re.M).search("ba", 1).group()
# re.compile("^a", re.M).search("ba", 1).span()
#
#
# p = re.compile("a[bcde]*e")
# print(p.match("abcdedcba").group())
# print(p.match("abcdedcba").span())
# #
# result = p.findall("abqexace_adceaede")
# print(result)
#
# p = re.compile("[ab]*[cd]{1,3}")
# m = p.match("bbacde")
# if m:
#     print('Match found: ', m.group(), m.span())
# else:
#     print('No match')
#
# it = p.finditer("aabbccddeeccaaeeddaabbccww")
# for i in it:
#     print(i.span(), i.group())
# print(p.findall("aabbccddeeccaaeeddaabbccww"))

# # match i search to nie to samo
print(re.match('super', 'superstition').span())
print(re.match('super', 'insuperable'))

print(re.search('super', 'superstition').span())
print(re.search('super', 'insuperable').span())
result = re.search('super', 'insuperable')
print( result.span(), result.start(), result.end())
