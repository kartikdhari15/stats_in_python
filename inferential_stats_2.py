# T-test
import numpy as np
from scipy.stats import ttest_1samp
ages=[4,5,3,4,8,5,6,7,3,2,5,8,6,9,9,2,1,2,6,5,3,4,9,8,7] # Consider this to be the population
ages_mean=np.mean(ages)
#print(ages_mean)
sample_size=10
ages_sample=np.random.choice(ages,sample_size) # Creation of sample from the population
#print(ages_sample)
ages_sample_mean=np.mean(ages_sample)
#print(ages_sample_mean)
print(ttest_1samp(ages_sample,5)) # (Sample varible,ages_mean(Population mean))