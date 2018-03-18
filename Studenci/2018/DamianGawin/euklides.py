a = input("podaj a: ")
b = input("podaj b: ")

def algor(a,b):
    if b != 0:
        b = a % b
        return (str(b))

print algor(a,b)
