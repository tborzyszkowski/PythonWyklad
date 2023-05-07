# podnoszenie bledow

except_object = NameError('-- ale blad przed try-except --')
try:
    # raise NameError('-- ale blad--')
    raise except_object
except NameError as e:
    print('+++Byl blad ale go juz nie ma+++:', e)
    raise  # i znow jest

# try:
#     raise KeyboardInterrupt
# except ValueError:
#     print('aaa')
# finally:
#     print('Goodbye, world!')
