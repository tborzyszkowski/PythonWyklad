# -*- coding: utf-8 -*-

import numpy as np
import statsmodels.api as sm
from statsmodels.graphics.gofplots import qqplot_2samples
from matplotlib import pyplot as plt
###################################################
# QQ-plot

x = np.random.normal(loc=8.5, scale=2.5, size=37)
y = np.random.normal(loc=8.0, scale=3.0, size=37)
pp_x = sm.ProbPlot(x)
pp_y = sm.ProbPlot(y)
fig = qqplot_2samples(pp_x, pp_y, xlabel="N(8.5,2.5)", ylabel="N(8,3)", line=None, ax=None)
fig.show(warn=True)
raw_input("Enter: ")
