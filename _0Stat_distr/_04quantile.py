# -*- coding: utf-8 -*-

from scipy import stats
import numpy as np
from scipy.stats.mstats import mquantiles

###################################################
# Percent Point Function (PPF) for distribution
# (Inverse of CDF: Cumulative Distribution Function
mu, sigma = 0, 1 # mean and standard deviation
print stats.norm.ppf( [.01, .05,.5, .95, .99], mu, sigma)

######################################
# Zadania
# 1. Policz ppf dla dla rozkładu t_Studenta o n stopniach swobody
#    (wykonać proby dla kilku n)
# 2. Jak w zadaniu 1. z tym, że dla skośniego rozkładu t_Studenta



###################################################
# Empirical Percent Point Function (PPF) for distribution


# s = np.array([6., 47., 49., 15., 42., 41., 7., 39., 43., 40., 36.])
s = np.random.normal(mu, sigma, 1000)
print mquantiles(s ,[.01, .05,.5, .95, .99])

######################################
# Zadanie
# 1. Sprawdzić zgodność kwantyli danych empirycznych z danymi rzeczywistymi
#    dla rozkładow:  t_Studenta i skośniego rozkładu t_Studenta
