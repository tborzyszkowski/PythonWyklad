# podnoszenie bledow
import sys

except_object = NameError('-- ale blad przed try-except --')
try:
    # raise NameError('-- ale blad--')
    raise except_object
except NameError as e:
    # print('+++Byl blad ale go juz nie ma+++:', e)
    (v1, v2, v3) = sys.exc_info()
    print((v1, v2, v3))
    for v in (v1, v2, v3):
        print(v)
        print(dir(v))
    # print(e.with_traceback(v3))
    # raise  # i znow jest

# try:
#     raise KeyboardInterrupt
# except ValueError:
#     print('aaa')
# finally:
#     print('Goodbye, world!')
