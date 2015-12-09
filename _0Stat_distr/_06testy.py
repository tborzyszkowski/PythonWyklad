# -*- coding: utf-8 -*-

from scipy import stats

# test KS
print stats.kstest(stats.norm.rvs(size=100), 'norm')

# T-Test
rvs1 = stats.norm.rvs(loc=5,scale=10,size=500)
rvs2 = (stats.norm.rvs(loc=5,scale=10,size=500) +
        stats.norm.rvs(scale=0.2,size=500))

print "ttest_rel: ", stats.ttest_rel(rvs1,rvs2)

rvs3 = (stats.norm.rvs(loc=8,scale=10,size=500) +
        stats.norm.rvs(scale=0.2,size=500))

print "ttest_rel2:",stats.ttest_rel(rvs1,rvs3)
