# Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?

import pandas as pd

DataBase = pd.read_csv('DataBases/adult.csv')

ValoresAusentes = DataBase.isna()
print(ValoresAusentes)

TratarValoresAusentes = DataBase.fillna(0, inplace= True)

