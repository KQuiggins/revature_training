class Product:
    """A product in the inventory.

    Must implement these dunder methods:
        __str__     — "Laptop ($999.99) — 15 in stock"
        __repr__    — "Product('Laptop', 999.99, stock=15, category='electronics')"
        __eq__      — Equal if same name AND category
        __lt__      — Compare by price (enables sorting)
        __hash__    — Based on name + category (enables use in sets)
        __bool__    — True if in stock (stock > 0)
        __contains__ — Check if substring in product name

    Class attributes:
        total_products (int): Count of all Product instances
    """
    total_products = 0

    def __init__(self, name, price, stock=0, category="general"):

        self.name = name
        self.price = price
        self.stock = stock