import numpy as np
import matplotlib.pyplot as plt
import statistics
import seaborn as sns

df=sns.load_dataset('tips')
#print(df.head())
#print(np.mean(df['total_bill']))
#print(np.median(df['total_bill']))
#print(statistics.mode(df['total_bill']))
#sns.boxplot(df['total_bill'])
#sns.histplot(df['total_bill'],kde=True)
#kde stands for kernel density estimation
#Creation of a pdf(probability density function)
#plt.show()

df1=sns.load_dataset('iris')
#print(df1.head())
#sns.histplot(df1['sepal_width'],kde=True)
#Follows Gaussian/Normal Distribution
#sns.countplot(df1['species'])
#plt.show()

print(np.percentile(df1['sepal_length'],[25,75]))