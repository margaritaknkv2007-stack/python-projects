import matplotlib.pyplot as plt

print("Введите числа через пробел:")

user_input = input("Ваши данные: ")
data = list(map(float, user_input.split()))

labels = [f"Столбец {i+1}" for i in range(len(data))] # создаем список подписей

plt.figure(figsize=(12, 8))

bars = plt.barh(labels, data, color='lightblue', height=0.6, edgecolor='black') # функция для горизонтальных столбцов

plt.xlabel('Значения', fontsize=12)
plt.ylabel('Столбцы', fontsize=12)
plt.title('Горизонтальная столбчатая диаграмма', fontsize=14, pad=20)
plt.grid(True, axis='x', linestyle='--', alpha=0.3)

# подписываем значения на столбцах
for bar, value in zip(bars, data): # объединяем столбцы и их значения
    width = bar.get_width() 
    plt.text(width + 0.5, bar.get_y() + bar.get_height()/2,  # добавляем текст на график
             f'{value}', ha='left', va='center', fontsize=10, fontweight='bold')
    
plt.show()