import numpy as np
import matplotlib.pyplot as plt

data = np.random.rand(10, 10) # функция для генерации случайных чисел

plt.figure(figsize=(10, 8))

heatmap = plt.imshow(data, cmap='viridis', interpolation='nearest') # функция для отображения изображений или матриц
                            # цветовая карта # сглаживание пикселей

plt.colorbar(heatmap, label='Value') # создаем цветовую шкалу

plt.xticks(range(10))
plt.yticks(range(10))
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Тепловая карта для матрицы 10x10', fontsize=14, pad=20)

plt.show()