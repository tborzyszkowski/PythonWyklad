# rok1 = 1990
# miesiac1 = 12
# dzien1 = 24
#
# rok2 = 1990
# miesiac2 = 10
# dzien2 = 24

dwieDaty = ({"rok": 1990, "miesiac": 9, "dzien": 24}, {"rok": 1990, "miesiac": 9, "dzien": 24})

if dwieDaty[0]["rok"] < dwieDaty[1]["rok"]:
    print "pierwsza wczesniejsza"
elif dwieDaty[0]["rok"] > dwieDaty[1]["rok"]:
    print "druga wczesniejsza"
else:
    if dwieDaty[0]["miesiac"] < dwieDaty[1]["miesiac"]:
        print "pierwsza wczesniejsza"
    elif dwieDaty[0]["miesiac"] > dwieDaty[1]["miesiac"]:
        print "druga wczesniejsza"
    else:
        if dwieDaty[0]["dzien"] < dwieDaty[1]["dzien"]:
            print "pierwsza wczesniejsza"
        elif dwieDaty[0]["dzien"] > dwieDaty[1]["dzien"]:
            print "druga wczesniejsza"
        else:
            print "daty sa rowne"


pierwszaData = dwieDaty[0]["rok"]*(10**4)+dwieDaty[0]["miesiac"]*(10**2)+dwieDaty[0]["dzien"]
drugaData = dwieDaty[1]["rok"]*(10**4)+dwieDaty[1]["miesiac"]*(10**2)+dwieDaty[1]["dzien"]

print pierwszaData
print drugaData

if pierwszaData < drugaData:
    print "pierwsza"
elif pierwszaData > drugaData:
    print "druga"
else:
    print "rowne"