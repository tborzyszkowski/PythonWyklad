# -*- coding: utf-8 -*-

from scipy import stats
import numpy as np
import time

#############################################
# obliczanie parametrow proby
# średnia, odchylenie odchylenie standardowe, skośność, kurtoza

test_start_time=time.time()

mu, sigma = 0, 1 # mean and standard deviation
s = np.random.normal(mu, sigma, 1000 * 1000 * 100)

n, (smin, smax), sm, sv, ss, sk = stats.describe(s)
#n, (smin, smax), sm, sv, ss, sk = stats.describe([1,2,3])

test_stop_time=time.time()

sstr = 'mean = %6.4f, variance = %6.4f, skew = %6.4f, kurtosis = %6.4f'

print 'sample params:'
print sstr %(sm, sv, ss, sk)
print 'time:', test_stop_time - test_start_time
######################################
# Zadania
# 1. Policzyć parametry rozkładu jak powyżej
#    dla rozkładu t_Studenta o n stopniach swobody (wykonać proby dla kilku n)
# 2. Jak w zadaniu 1. z tym, że dla skośniego rozkładu t_Studenta
