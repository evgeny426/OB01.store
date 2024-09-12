# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности,
# но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать
# класс `Store`, который можно будет использовать для создания различных магазинов.
#
# Шаги:
# 1. Создай класс `Store`:
# -Атрибуты класса:
# - `name`: название магазина.
# - `address`: адрес магазина.
# - `items`: словарь, где ключ - название товара, а значение - его цена. Например, `{'apples': 0.5, 'bananas': 0.75}`.
# - Методы класса:
# - `__init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items`.
# -  метод для добавления товара в ассортимент.
# - метод для удаления товара из ассортимента.
# - метод для получения цены товара по его названию. Если товар отсутствует, возвращайте `None`.
# - метод для обновления цены товара.
# 2. Создай несколько объектов класса `Store`:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.


class Store():

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_and_update_item(self, name, price):
        self.items[name] = price

    def del_item(self, name):
        del self.items[name]

    def get_price(self, name):
        return self.items.get(name)

# Создаём три магазина
store1 = Store("Большой магазин", "Дальняя улица")
store2 = Store("Средний магазин", "Средняя улица")
store3 = Store("Маленький магазин", "Ближняя улица")

# Добавляем товары в магазины
store1.add_and_update_item("apples", 0.5)
store1.add_and_update_item("orange", 0.4)

store2.add_and_update_item("cherry", 0.1)
store2.add_and_update_item("peach", 0.25)

store3.add_and_update_item("grape", 0.15)
store3.add_and_update_item("strawberry", 0.34)

# Добавляем товар в "Большой магазин"
print(f"Store Items: {store1.items}")
store1.add_and_update_item("mandarin", 0.2)
print(f"Store Items: {store1.items}")

# Обновляем цену на товар в "Большом магазине"
store1.add_and_update_item("mandarin", 0.45)
print(f"Store Items: {store1.items}")

# Удаляем товар в "Большом магазине"
store1.del_item("mandarin")
print(f"Store Items: {store1.items}")

# Запрашиваем цену на товар в "Большом магазине"
price = store1.get_price("orange")
print(f"Price: {price}")
