# Suppose the IQ scores of a certain population follow a normal distribution
# with a mean of 100 and a standard deviation of 15.
# A researcher wants to know if a new drug affects IQ levels, so he recruits
# 20 patients to try it and records their IQ levels.
# Perform a one sample z-test to determine whether the new drug causes
# difference in IQ levels.

from statsmodels.stats.weightstats import ztest as ztest
data=[88,92,94,94.96,97,97,97,99,99,105,109,109,109,110,112,112,113,114,115]
print(ztest(data,value=100))

# z test value=1.77>0.9616
# Reject Null Hypothesis-Mean is 100(as number from table is smaller than that of z test value)
# Therefore no difference in IQ levels.