# petla z wyjatkami

# print('1'*20)

# while True:
#     try:
#         x = int(input("Podaj liczbe: "))
#         y = 1 / x
#         print(y)
#         break
#     except ValueError:
#         print("+++ Chodzilo o liczbe +++")
#     except ZeroDivisionError as e:
#         print(e)


# pliki i wyjatki
# print '2'*20
#
# import sys
#
# try:
#     f = open('myfile.txt')
#     s = f.readline()
#     print(s.strip())
#     i = int(s.strip())
#     i = 1/i
#     # raise NameError
# except IOError as e:
#     print("I/O error(%s): %s" % e)
# except ValueError:
#     print("Could not convert data to an integer.")
# except ZeroDivisionError as e:
#     print("ZeroDivisionError:", e)
# except Exception as e:
#     print("Unexpected error:", sys.exc_info()) # [0]
#     print(type(e))
#     # raise
# else:
#     print("Else part")

# #
# print '3'*20
#
# import sys
#
# for arg in sys.argv[1:]:
#     try:
#         f = open(arg, 'r')
#     except IOError:
#         print('cannot open', arg)
#     else:
#         print(arg, 'has', len(f.readlines()), 'lines')
#         f.close()

# # Szczegoly wyjatku
# print '4'*20
#
# try:
#     raise Exception('spam', 'eggs', 333)
# except Exception as inst:
#     print(type(inst))     # the exception instance
#     print(inst.args)     # arguments stored in .args
#     print(inst)           # __str__ allows args to printed directly
#     x, y, q = inst.args          # __getitem__ allows args to be unpacked directly
#     print('x =', x)
#     print('y =', y)
#     print('q =', q)

#
# #
#
# print '5'*20
#
# def this_fails():
#     return 1/0
#
#
# try:
#     this_fails()
# except ZeroDivisionError as detail:
#     print('Handling run-time error:', detail)
# this_fails()

# Bind the name getpass to the appropriate function
# print '6'*20
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
#             print("No AskPassword")
#         else:
#             # getpass = AskPassword
#             print("AskPassword")
#     else:
#         # getpass = win_getpass
#         print("win_getpass")
# else:
#     # getpass = unix_getpass
#     print("unix_getpass")

def exception_return():
    result = 1
    try:
        result += 1
        print("try", result)
        return result
        raise
        # y = 1 / 0
    except ZeroDivisionError as e:
        result += 1
        print("except", result)
        print(e)
    except NameError:
        print("NameError")
        raise
    finally:
        result += 1
        print("finally", result)
        # return result


a = exception_return()
print(a)