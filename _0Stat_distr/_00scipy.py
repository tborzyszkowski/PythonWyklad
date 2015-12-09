# http://docs.scipy.org/doc/scipy/reference/tutorial/stats.html
# import scipy
# print dir(scipy)
#import scipy.stats
from scipy import stats
from scipy.stats import norm
print norm.__doc__

print 'bounds of distribution lower: %s, upper: %s' % (norm.a,norm.b)

rv = norm()
print dir(rv)

# distributions
import warnings
warnings.simplefilter('ignore', DeprecationWarning)
dist_continu = [d for d in dir(stats) if
                isinstance(getattr(stats,d), stats.rv_continuous)]
dist_discrete = [d for d in dir(stats) if
                isinstance(getattr(stats,d), stats.rv_discrete)]
print 'number of continuous distributions:', len(dist_continu)
print 'number of discrete distributions:  ', len(dist_discrete)
# print dist_continu
# print dist_discrete

# cdf: Cumulative Distribution Function

print norm.cdf(0)
print norm.cdf([-1., 0, 1])
