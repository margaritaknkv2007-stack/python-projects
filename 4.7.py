import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D # 3D-модуль для объемных графиков

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)

Z = np.sin(np.sqrt(X**2 + Y**2))

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d') # добавляем 3D-оси

# Рисуем поверхность
surface = ax.plot_surface(X, Y, Z, cmap='viridis', alpha=0.9, # метод 3D-осей
linewidth=0, antialiased=True)

ax.set_xlabel('Ось X', fontsize=10, labelpad=8)
                                    # отступ подписей от осей
ax.set_ylabel('Ось Y', fontsize=10, labelpad=8)
ax.set_zlabel('Ось Z', fontsize=10, labelpad=8)
ax.set_title('3D: z = sin(sqrt(x² + y²))', fontsize=12, pad=15)  

colorbar = fig.colorbar(surface, ax=ax, shrink=0.5, aspect=15)
colorbar.set_label('Z', fontsize=10)

plt.show()