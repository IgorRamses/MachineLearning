# Utilizando o matplotlib, utilize a função subplot() para mostrar 6 gráficos.
import matplotlib.pyplot as plt

plt.figure(figsize=(12, 8)) 
plt.suptitle("Exemplo de Subplots", fontsize=16)

plt.subplot(2, 3, 1)
plt.plot([0, 1], [0, 1])
plt.title("Subplot 1")

plt.subplot(2, 3, 2)
plt.plot([0, 1], [0, 2])
plt.title("Subplot 2")

plt.subplot(2, 3, 3)
plt.plot([0, 1], [0, 3])
plt.title("Subplot 3")

plt.subplot(2, 3, 4)
plt.plot([0, 1], [0, 4])
plt.title("Subplot 4")

plt.subplot(2, 3, 5)
plt.plot([0, 1], [0, 5])
plt.title("Subplot 5")

plt.subplot(2, 3, 6)
plt.plot([0, 1], [0, 6])
plt.title("Subplot 6")

plt.show()