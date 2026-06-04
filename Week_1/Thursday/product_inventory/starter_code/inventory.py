from collections import deque

class Inventory:
    """A collection of products with search, filter, and transaction capabilities.

    Features:
        - Add/remove products
        - Search by name or category
        - Transaction history (deque with maxlen=50)
        - Restock and sell operations with exception handling
    """

    def __init__(self):
        self.products = {}          # {product_id: Product}
        self.categories = set()     # Unique categories
        self.history = deque(maxlen=50)  # Recent transactions
        self._next_id = 1

    def add_product(self, product):
        """Add a product to inventory. Return the assigned ID."""
        pass  # TODO

    def remove_product(self, product_id):
        """Remove a product. Raise ProductNotFoundError if missing."""
        pass  # TODO

    def get_product(self, product_id):
        """Get a product by ID. Raise ProductNotFoundError if missing."""
        pass  # TODO

    def sell(self, product_id, quantity):
        """Sell units of a product.
        Raise ProductNotFoundError if ID doesn't exist.
        Raise InsufficientStockError if not enough stock.
        Record transaction in history.
        """
        pass  # TODO

    def restock(self, product_id, quantity):
        """Add stock. Raise ProductNotFoundError if missing."""
        pass  # TODO

    # --- Comprehension-powered queries ---

    def search(self, keyword):
        """Return products containing keyword (case-insensitive).
        Use a list comprehension and the __contains__ dunder.
        """
        pass  # TODO

    def by_category(self, category):
        """Return products in a category. Use a list comprehension."""
        pass  # TODO

    def in_stock(self):
        """Return products with stock > 0. Use __bool__ dunder + filter."""
        pass  # TODO

    def price_range(self, min_price, max_price):
        """Return products in the price range. Use a list comprehension."""
        pass  # TODO

    def summary(self):
        """Return a dict with:
        - total_products
        - total_value (sum of price * stock for each product)
        - categories (sorted list)
        - out_of_stock_count
        Use dict/list comprehensions.
        """
        pass  # TODO