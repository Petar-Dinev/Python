from project.product import Product


class ProductRepository:
    def __init__(self):
        self.products: list[Product] = []

    def add(self, product: Product) -> None:
        self.products.append(product)

    def find(self, product_name: str) -> Product:
        return next((p for p in self.products if p.name == product_name), None)

    def remove(self, product_name: str) -> None:
        product = next((p for p in self.products if p.name == product_name), None)
        if product:
            self.products.remove(product)

    def __repr__(self):
        return '\n'.join([f"{p.name}: {p.quantity}" for p in self.products])
