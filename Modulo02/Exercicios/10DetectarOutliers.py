#Utilizando pandas, mostre uma forma de detectar e tratar valores outliers em um DataFrame.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

DataBase = pd.read_csv('Databases/adult.csv')

plt.boxplot(DataBase['age'])
plt.show()

median = np.median(DataBase['age'])
mad = np.median(np.abs(DataBase['age'] - median))
limite_mad = 3.5

DataBaseSemOutliers = DataBase[np.abs(DataBase['age'] - median) / mad <= limite_mad]

plt.boxplot(DataBaseSemOutliers['age'])
plt.show()