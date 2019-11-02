# petla z wyjatkami

# print '1'*20

# while True:
#     try:
#         x = int(raw_input("Podaj liczbe: "))
#         y = 1 / x
#         print y
#         break
#     except ValueError:
#         print "+++ Chodzilo o liczbe +++"
#     except ZeroDivisionError, e:
#         print e


# pliki i wyjatki
# print '2'*20
#
# import sys
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     print s.strip()
#     i = int(s.strip())
#     i = 1/i
# except IOError, (errno, strerror):
#     print "I/O error(%s): %s" % (errno, strerror)
# except ValueError:
#     print "Could not convert data to an integer."
# except ZeroDivisionError, e:
#     print "ZeroDivisionError:", e
# except:
#     print "Unexpected error:", sys.exc_info()  # [0]
#     # raise
# else:
#     print "Else part"

# #
# print '3'*20
#
# import sys
#
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print 'cannot open', arg
#     else:
#         print arg, 'has', len(f.readlines()), 'lines'
#         f.close()

# # Szczegoly wyjatku
# print '4'*20
#
# try:
#     raise Exception('spam', 'eggs',444)
# except Exception, inst:
#     print type(inst)     # the exception instance
#     print inst.args      # arguments stored in .args
#     print inst           # __str__ allows args to printed directly
#     x, y, q = inst          # __getitem__ allows args to be unpacked directly
#     print 'x =', x
#     print 'y =', y
<<<<<<< HEAD
#     print 'q =', q

=======
#
>>>>>>> remotes/origin/master
# #
#
# print '5'*20
#
# def this_fails():
#     return 1/0
#
# try:
#     this_fails()
# except ZeroDivisionError, detail:
#     print 'Handling run-time error:', detail
<<<<<<< HEAD
#

# Bind the name getpass to the appropriate function
# print '6'*20
=======

>>>>>>> remotes/origin/master
#
# try:
#     import termios
#     import TERMIOS
# except ImportError:
#     try:
#         import msvcrt
#     except ImportError:
#         try:
#             from EasyDialogs import AskPassword
#         except ImportError:
#             # getpass = default_getpass
#             print "No AskPassword"
#         else:
#             # getpass = AskPassword
#             print "AskPassword"
#     else:
#         # getpass = win_getpass
#         print "win_getpass"
# else:
#     # getpass = unix_getpass
#     print "unix_getpass"
