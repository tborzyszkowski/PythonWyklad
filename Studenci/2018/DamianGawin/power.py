a = raw_input("Enter the number: ")
b = raw_input("Enter second number: ")

if a == b:
    print "true"
elif int(b) == int(a) * int(a):
    print "true"
else:
    print "false"