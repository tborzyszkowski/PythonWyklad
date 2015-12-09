# -*- coding: utf-8 -*-

from scipy import stats
import numpy as np
import matplotlib.pyplot as plt

# dostępne funkcje
# print norm.__doc__

###################################
# Generowanie probek losowych dla rozkładu normalnego
#

mu, sigma = 0, 0.1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000)
# print s

#Verify the mean and the variance
print "Mean: ", abs(mu - np.mean(s)) < 0.01, np.mean(s)
print "Var:  ", abs(sigma - np.std(s, ddof=1)) < 0.01, np.std(s, ddof=1)

count, bins, ignored = plt.hist(s, 50, normed=True)
# print "Count:", count
# print "Bins: ", bins
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
                np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
          linewidth=2, color='r')
plt.grid(True)
plt.show()

# Więcej o rysowaniu wykresow na stronie:
# http://matplotlib.org/users/pyplot_tutorial.html

######################################
# Zadania
# 1. Narysowac podobny wykres dla rozkładu t_Studenta o n stopniach swobody
#    (wykonać proby dla kilku n)
#    Wygeneruj probki w oparciu o:
#    http://docs.scipy.org/doc/numpy-1.10.1/reference/generated/numpy.random.standard_t.html#numpy.random.standard_t
#
# 2. Jak w zadaniu 1. z tym, że dla skośniego rozkładu t_Studenta
#    Wygeneruj probki w oparciu o: metodę rsv klasy SkewStudent (plik SkewStudent.py)
