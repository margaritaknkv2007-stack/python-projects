import matplotlib.pyplot as plt

categories = ['Фильмы', 'Музыка', 'Книги', 'Игры', 'Спорт']
preferences = [30, 25, 15, 20, 5]

# Цвета для каждой категории
colors = ['red', 'blue', 'green', 'orange', 'purple']

plt.figure(figsize=(10, 8)) 

# Автоматическое создание explode
explode_values = [0.05 for _ in categories]

plt.pie(preferences, labels=categories, colors=colors, autopct='%1.1f%%', 
        startangle=90, explode=explode_values)

plt.title('Предпочтения пользователей по категориям', fontsize=14, pad=20)

plt.show()