# petla z wyjatkami

print '1'*20

while True:
    try:
        x = int(raw_input("Podaj liczbe: "))
        break
    except ValueError:
        print "+++ Chodzilo o liczbe +++"


# pliki i wyjatki
print '2'*20

import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
    i = 1/0
except IOError, (errno, strerror):
    print "I/O error(%s): %s" % (errno, strerror)
except ValueError:
    print "Could not convert data to an integer."
except:
    print "Unexpected error:", sys.exc_info()#[0]
    #raise
else:
    print "Else part"

#
print '3'*20

for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()

# Szczegoly wyjatku
print '4'*20

try:
    raise Exception('spam', 'eggs')
except Exception, inst:
    print type(inst)     # the exception instance
    print inst.args      # arguments stored in .args
    print inst           # __str__ allows args to printed directly
    x, y = inst          # __getitem__ allows args to be unpacked directly
    print 'x =', x
    print 'y =', y

#

print '5'*20

def this_fails():
    x = 1/0

try:
    this_fails()
except ZeroDivisionError, detail:
    print 'Handling run-time error:', detail


# Bind the name getpass to the appropriate function
# print '6'*20
# 
# try:
#       import termios, TERMIOS                     
# except ImportError:
#       try:
#           import msvcrt                           
#       except ImportError:
#           try:
#               from EasyDialogs import AskPassword 
#           except ImportError:
#               getpass = default_getpass           
#           else:                                   
#               getpass = AskPassword
#       else:
#           getpass = win_getpass
# else:
#     getpass = unix_getpass

      