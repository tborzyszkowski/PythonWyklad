# Napisy
print '----------'
# podobnie jak w C uzywamy \n \t \" ....
print 'Ala\t i \n Ola'
print '\'Ala\' - powiedziala Ola'

# laczenie napisow
a = 'Ala\t'+'i '+'Ola '
print a[4]
print a * 3
print type(a)
# typy nie sa przypisane zmiennym na zawsze
a=3
print type(a)

# lista operacji na napisach
import string
# lista operacji udostepnionych przez modul string
print dir(string)

# opis funkcji count
print string.count.func_doc
          
# napisy formatowane

a = 'Ala'
b = 'As'
print "%s i %s" % (a, b)
print "%d + %d = %d" %(3, 4, 3+4)
print "Cena = %f"    % 50.456789
print "Cena = %.2f"  % 50.456789
print "Cena = %+.3f" % 50.456789
print '%(language)s has %(#)03d quote types.' % \
          {'language': "Python", "#": 2}

