import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('iris')
#print(df.head(),df.tail(),f"Shape:{df.shape}",sep='\n')
#print(df.corr())
sns.pairplot(df)
plt.show()