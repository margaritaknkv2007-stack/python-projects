import numpy as np
import matplotlib.pyplot as plt

x1 = np.random.normal(2, 0.5, 50)
y1 = np.random.normal(2, 0.5, 50)

x2 = np.random.normal(5, 0.5, 50)
y2 = np.random.normal(3, 0.5, 50)

x3 = np.random.normal(3, 0.5, 50)
y3 = np.random.normal(6, 0.5, 50)

plt.figure(figsize=(10, 8)) # функция для создания нового холста

plt.scatter(x1, y1, color='blue', label='Кластер 1', alpha=0.7, s=50) # функция для точечной диаграммы
plt.scatter(x2, y2, color='red', label='Кластер 2', alpha=0.7, s=50)
plt.scatter(x3, y3, color='green', label='Кластер 3', alpha=0.7, s=50)

plt.xlabel('X координата', fontsize=12)
plt.ylabel('Y координата', fontsize=12)
plt.title('Точечная диаграмма с тремя кластерами', fontsize=14)
plt.legend(fontsize=10)
plt.grid(True, linestyle='--', alpha=0.3)

plt.show()