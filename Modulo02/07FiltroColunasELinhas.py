# Utilizando pandas, como selecionar uma coluna específica e filtrar linhas em um “DataFrame” com base em uma condição?

import pandas as pd

DataBase = pd.read_csv('Databases/auto-mpg.csv')

ColunaDeQuantidadeDeCilindros = DataBase.iloc[:,1].values

ColunaDeQuantidadeDeCilindrosFiltrada = ColunaDeQuantidadeDeCilindros[ColunaDeQuantidadeDeCilindros > 4]

print(f'Numeros presentes na coluna: {ColunaDeQuantidadeDeCilindros}')

print(f'Filtragem de numeros acima de 4: {ColunaDeQuantidadeDeCilindrosFiltrada}')