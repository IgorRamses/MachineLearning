#Utilizando pandas, como remover uma coluna de um DataFrame?

import pandas as pd

DataBase = pd.read_csv('Databases/adult.csv')

RemovendoColuna = DataBase.drop(DataBase.columns[1], axis = 1, inplace = True)

print(DataBase)