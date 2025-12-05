import numpy as np
import matplotlib.pyplot as plt

# функции
def z1(alpha):
    return np.sin(alpha) + np.cos(2*alpha) + np.cos(6*alpha) + np.cos(7*alpha) + 10

def z2(alpha):
    return 4 * np.cos(alpha/2) * np.cos(5*alpha/2) * np.cos(4*alpha)

# данные
alpha = np.linspace(0, 5, 100)
z1_values = z1(alpha)
z2_values = z2(alpha)

fig, ax1 = plt.subplots(figsize=(12, 8)) # создаем окно 12 на 8 для графика

ax1.grid(True, linestyle='--', alpha=0.7) # добавляем сетку, прозрачность альфа 70%

# первая функция
ax1.set_xlabel('α (альфа)', fontsize=12)
ax1.set_ylabel('z₁(α)', color='blue', fontsize=12)
line1 = ax1.plot(alpha, z1_values, 'blue', linewidth=2, label='z₁(α) = cosα + cos2α + cos6α + cos7α')
ax1.tick_params(axis='y', labelcolor='blue')

# вторая функция
ax2 = ax1.twinx()
ax2.set_ylabel('z₂(α)', color='red', fontsize=12)
line2 = ax2.plot(alpha, z2_values, 'red', linewidth=2, label='z₂(α) = 4cos(α/2)cos(5α/2)cos(4α)')
ax2.tick_params(axis='y', labelcolor='red')

# легенда
lines = line1 + line2
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc='upper right', fontsize=10)

# заголовок
plt.title('Графики функций z₁(α) и z₂(α)', fontsize=14, pad=20)

# подписи на графике
ax1.text(1.0, 2.0, 'z₁(α)', color='blue', fontsize=12, fontweight='bold')
ax2.text(3.5, -2.5, 'z₂(α)', color='red', fontsize=12, fontweight='bold')

plt.show()
