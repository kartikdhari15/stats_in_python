import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=[-3,2,1,2,2,3,3,5,5,5,4,6,6,6,7,8,8,9,27,6]
outliers=[]
df=sorted(df)
q1,q3=np.percentile(df,[25,75])
iqr=q3-q1
l_fence=q1-1.5*iqr
h_fence=q3+1.5*iqr
print("Range:",l_fence,"to",h_fence)
for i in df:
    if i<l_fence or i>h_fence:
        outliers.append(i)
print("Outliers:",outliers)
sns.boxplot(df)
plt.show()