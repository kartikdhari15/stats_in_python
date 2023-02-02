#Data Points beyond the 3rd Standard Deviation can be considered
#as an outlier by 68-95-99.7% Rule
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
dataset=[1,2,2,2,2,2,2,1,1,1,2,2,2,4.29]
outliers=[]

def detect_outliers(data):
    threshold=3
    mean=np.mean(data)
    std=np.std(data)
    for i in data:
        z_score=(i-mean)/std
        #print(z_score)
        if np.abs(z_score)>threshold:
            outliers.append(i)
    return outliers

print("Outliers:",detect_outliers(dataset))
#sns.histplot(dataset)
sns.boxplot(dataset)
plt.show()