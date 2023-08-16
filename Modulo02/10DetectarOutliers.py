#Utilizando pandas, mostre uma forma de detectar e tratar valores outliers em um DataFrame.

import pandas as pd
import matplotlib.pyplot as plt

DataBase = pd.read_csv('Databases/adult_census.csv')

plt.boxplot(DataBase['AGE'])
plt.show()