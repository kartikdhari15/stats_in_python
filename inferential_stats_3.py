import numpy as np
import pandas as pd
import scipy.stats as stats
import math
np.random.seed(6) # If called with same value/parameter(6) returns same set of random numbers everytime
school_ages=stats.poisson.rvs(loc=18,mu=35,size=1500) # Starting age=18,mean=35,size or no of ages=1500
classA_ages=stats.poisson.rvs(loc=18,mu=30,size=60) # Starting age=18,mean=30,size or no of ages=60
#print(school_ages,classA_ages,sep='\n')
#print(school_ages.mean(),classA_ages.mean(),sep='\n')
_,p_value=stats.ttest_1samp(classA_ages,school_ages.mean())
#print(p_value)
# Conclusion:Both mean are too far from each other
if p_value<=0.05: # 0.05 is significance value
    print("H0 Rejected")
else:
    print("H0 Accepted")