# import a01nazwa
#
# a01nazwa.nazwa()

print(__name__)
print(type(__name__))

a = 13


def nazwa():
    print(__name__)
    variable_a = 1
    print("variable_a = ", variable_a)


if __name__ == "__main__":
    print('aqq')
    nazwa()
    print('a = ', a)
