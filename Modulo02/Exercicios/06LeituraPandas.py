# Utilizando pandas, como realizar a leitura de um arquivo CSV em um DataFrame e exibir as primeiras linhas?

import pandas as pd

DataBase = pd.read_csv('Databases/adult.csv')

print(DataBase.head(5))