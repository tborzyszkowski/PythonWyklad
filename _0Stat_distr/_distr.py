# Gestosc rozkladu N(0,1)
# czyli:
# norm.pdf(x) = exp(-x**2/2)/sqrt(2*pi)

from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1, 1)
# mean, var, skew, kurt = norm.stats(moments='mvsk')
x = np.linspace(norm.ppf(0.001), norm.ppf(0.999), 1000)

ax.plot(x, norm.pdf(x), 'r-', lw=5, alpha=0.6, label='norm pdf')

plt.show()
