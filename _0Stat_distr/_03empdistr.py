# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from SkewStudent import SkewStudent

#############################################
# dystrybuanta empiryczna dla danej proby
def ecdf(x, sample):
    counter = 0.0
    for obs in sample:
        if obs <= x:
            counter += 1
    return counter / len(sample)


###############################################################
# dystrybuanta empiryczna i rzeczywista na jednym wykresie

# mu, sigma = 0, 5
# sample = np.random.normal(mu, sigma, 1000)
#
# x = np.linspace(min(sample), max(sample))
# y_ecdf = np.vectorize(lambda x: ecdf(x, sample))
# y_cdf  = stats.norm.cdf(x, loc=mu, scale=sigma)
# # print x
# # print y_ecdf
# plt.plot(x, y_ecdf(x), color="blue")
# plt.plot(x, y_cdf,  color="red")
# plt.show()

######################################
# Zadania
# 1. Narysuj dystrybuantę empiryczną i rzeczywistą na jednym wykresie
#    dla rozkładu t_Studenta o n stopniach swobody (wykonać proby dla kilku n)
# 2. Jak w zadaniu 1. z tym, że dla skośniego rozkładu t_Studenta

s = SkewStudent(eta=10., lam=-.1)
sample = s.rvs(size=100)
x = np.linspace(min(sample), max(sample))
y_ecdf = np.vectorize(lambda x: ecdf(x, sample))
y_cdf  = s.cdf(x)
# print x
# print y_ecdf
plt.plot(x, y_ecdf(x), color="blue")
plt.plot(x, y_cdf,  color="red")
plt.show()
