#importing statistics
import statistics as st
#importing pandas
import pandas as pd
#importing numpy
import numpy as np
#importing matplotlib
import matplotlib.pyplot as plt
#reading file
rf=pd.read_csv('tint.csv')
print(rf.info())
#checking for null values
rf.isnull().any()
ageQ1=np.quantile(rf['Age'], 0.25)
print(" Q1 is this ta da!!! " ,ageQ1)
#
ageQ2=np.quantile(rf['Age'], 0.50)
print(" Q2 is this ta da!!! " ,ageQ2)
#
ageQ3=np.quantile(rf['Age'], 0.75)
print(" Q3 is this ta da!!! " ,ageQ3)
#finding intel quantile
quare=ageQ3-ageQ1
print("the intel quantile range is this " ,quare)
#
#creating a histogram
plt.hist(rf['Age'])
plt.xlabel('Age')
plt.ylabel('count of age')
plt.show()
plt.boxplot(rf['Age'])
plt.show()