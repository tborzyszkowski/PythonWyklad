liczba = raw_input("liczba: ")
length = len(str(liczba))
y = []
name = ("zero", "jeden", "dwa", "trzy", "cztery", "piec", "szesc", "siedem", "osiem", "dziewiec")

for i in range(0, length):
    y.append(name[int(str(liczba)[i])])
print y
