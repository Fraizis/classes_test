from dataclasses import dataclass


class StockError(Exception):
    pass


@dataclass(frozen=True)
class Product:
    name: str
    price: float
    stock: int = 0


class ShoppingCart:
    def __init__(self):
        self._items = []

    def __str__(self):
        return f'В вашей корзине {len(self._items)} товаров на сумму {self.total_price} руб.'

    def __len__(self):
        return len(self._items)

    def add_product(self, product: Product):
        if not isinstance(product, Product) or product.stock <= 0:
            return StockError(f'Товар {product.name!r} отсутствует на складе.')

        self._items.append(product)
        product.stock -= 1

    @property
    def total_price(self):
        total_sum = sum(p.price for p in self._items)
        return total_sum

    @classmethod
    def from_products(cls, product_list: list):
        new_cart = cls()
        for p in product_list:
            new_cart.add_product(p)

        return new_cart


apples = Product('apple', 123, 3)
user_cart = ShoppingCart.from_products([apples, apples])
print(user_cart)
print(user_cart.total_price)
