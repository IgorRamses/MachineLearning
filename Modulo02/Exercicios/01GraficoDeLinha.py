#Utilizando o matplotlib, crie e mostre um gráfico de linha simples e adicione títulos aos eixos X e Y do gráfico.

import matplotlib.pyplot as plt

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho']
valores = [101235, 107697, 108256, 109236, 104859, 112986]

plt.plot(meses, valores)
plt.ylim(100000,115000)
plt.title("Faturamento do primeiro semestre de 2017")
plt.xlabel("Meses")
plt.ylabel("Faturamento")
plt.show()