import pytest


# Тестируемая система
class ShoppingCart:
    """Простая корзина покупок"""

    def __init__(self):
        self.items = []
        self.total = 0

    def add_item(self, name, price):
        self.items.append({"name": name, "price": price})
        self.total += price

    def remove_item(self, name):
        for item in self.items:
            if item["name"] == name:
                self.total -= item["price"]
                self.items.remove(item)
                break

    def clear(self):
        self.items = []
        self.total = 0


# Фикстура
@pytest.fixture
def cart():
    """
    Эта фикстура создаёт новую корзину ДО каждого теста и очищает её ПОСЛЕ каждого теста
    """

    cart = ShoppingCart()  # создаём объект

    # Добавляем базовые товары (подготовка)
    cart.add_item("Яблоко", 50)
    cart.add_item("Хлеб", 30)

    # Отдаём корзину тесту
    yield cart

    # Этот код выполнится ПОСЛЕ теста
    cart.clear()


# Тест
def test_add_item_to_cart(cart):
    """
    Тест 1: Добавляем товар в корзину
    Фикстура 'cart' автоматически передаётся сюда
    """

    initial_count = len(cart.items)
    initial_total = cart.total

    cart.add_item("Молоко", 80)

    assert len(cart.items) == initial_count + 1
    assert cart.total == initial_total + 80


# Тест
def test_remove_item_from_cart(cart):
    """
    Тест 2: Удаляем товар из корзины
    Используем ту же фикстуру 'cart' (НО НОВУЮ КОРЗИНУ!)
    """

    initial_count = len(cart.items)

    cart.remove_item("Яблоко")

    assert len(cart.items) == initial_count - 1
    assert cart.total == 30  # остался только хлеб за 30 руб


# Тест
def test_total_calculation(cart):
    """
    Тест 3: Проверяем общую сумму
    Снова используем ту же фикстуру 'cart'
    """

    assert cart.total == 80  # 50 (яблоко) + 30 (хлеб)

    cart.add_item("Икра", 1000)

    assert cart.total == 1080  # 80 + 1000
