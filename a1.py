import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df=pd.read_csv('FuelConsumption.csv')
print(df.head())

print(df.isnull().any())

print(df.info())

sns.scatterplot(x='FUELCONSUMPTION_COMB_MPG',y='CO2EMISSIONS',data=df)
plt.show()

sns.scatterplot(x='FUELCONSUMPTION_COMB_MPG',y='CO2EMISSIONS',hue='FUELTYPE',data=df)
plt.show()

sns.scatterplot(x='FUELCONSUMPTION_COMB_MPG',y='CO2EMISSIONS',hue='FUELTYPE',size='ENGINESIZE',data=df)
plt.show()

df=df.drop(['MAKE','MODEL','TRANSMISSION','VEHICLECLASS','FUELTYPE'],axis=1)
corr=df.corr()
sns.heatmap(corr,annot=True)
plt.show()
