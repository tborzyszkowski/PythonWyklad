# podnoszenie bledow

try:
    raise NameError('-- ale blad--')
except NameError:
    print('+++Byl blad ale go juz nie ma+++')
    raise  # i znow jest

# try:
#     raise KeyboardInterrupt
# except ValueError:
#     print 'aaa'
# finally:
#     print 'Goodbye, world!'
