from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from collections import OrderedDict


# ─── Product ─────────────────────────────────────────────────────────────────

@dataclass
class Product:
    id: int
    name: str
    category: str
    price: float          # USD
    emoji: str
    tag: str              # "sale", "new", or ""
    stars: int            # 1–5

    def __str__(self) -> str:
        star_str = "★" * self.stars + "☆" * (5 - self.stars)
        tag_str  = f" [{self.tag.upper()}]" if self.tag else ""
        return f"{self.name:<20} {self.category:<12} ${self.price:>6.2f}  {star_str}{tag_str}"


# ─── Cart ─────────────────────────────────────────────────────────────────────

class Cart:
    def __init__(self, catalog: dict[int, Product]) -> None:
        self._catalog: dict[int, Product] = catalog
        self._items: OrderedDict[int, int] = OrderedDict()  # product_id → qty

    def add_item(self, product_id: int) -> None:
        if product_id not in self._catalog:
            raise KeyError(f"Product ID {product_id} not found.")
        self._items[product_id] = self._items.get(product_id, 0) + 1

    def remove_item(self, product_id: int) -> None:
        if product_id not in self._items:
            raise KeyError(f"Product ID {product_id} not in cart.")
        if self._items[product_id] == 1:
            del self._items[product_id]
        else:
            self._items[product_id] -= 1

    def clear(self) -> None:
        self._items.clear()

    @property
    def total_items(self) -> int:
        return sum(self._items.values())

    @property
    def subtotal(self) -> float:
        return sum(
            self._catalog[pid].price * qty
            for pid, qty in self._items.items()
        )

    def print_receipt(self) -> None:
        if not self._items:
            print("  Cart is empty.")
            return
        w = 51
        print(f"  ┌{'─' * w}┐")
        print(f"  │{'CART RECEIPT':^{w}}│")
        print(f"  ├{'─' * w}┤")
        for pid, qty in self._items.items():
            p     = self._catalog[pid]
            total = p.price * qty
            print(f"  │  {p.name:<20} x{qty:<3}  ${total:>7.2f}          │")
        tax   = self.subtotal * 0.08
        grand = self.subtotal + tax
        print(f"  ├{'─' * w}┤")
        print(f"  │  {'Subtotal (' + str(self.total_items) + ' items)':<25}       ${self.subtotal:>7.2f}          │")
        print(f"  │  {'Tax (8%)':<25}       ${tax:>7.2f}          │")
        print(f"  │  {'TOTAL':<25}       ${grand:>7.2f}          │")
        print(f"  └{'─' * w}┘")


# ─── Store ────────────────────────────────────────────────────────────────────

class Store:
    NAV_CATEGORIES = ["All", "Electronics", "Fashion", "Home & Living", "Sports", "Beauty"]

    def __init__(self, name: str) -> None:
        self.name = name
        self._catalog: dict[int, Product] = {}

    def add_product(self, product: Product) -> None:
        self._catalog[product.id] = product

    @property
    def catalog(self) -> dict[int, Product]:
        return dict(self._catalog)

    def get_by_category(self, category: str) -> list[Product]:
        if category.lower() == "all":
            return list(self._catalog.values())
        return [p for p in self._catalog.values()
                if p.category.lower() == category.lower()]

    def get_by_tag(self, tag: str) -> list[Product]:
        return [p for p in self._catalog.values()
                if p.tag.lower() == tag.lower()]

    def new_cart(self) -> Cart:
        return Cart(self._catalog)

    def print_header(self) -> None:
        print("╔═══════════════════════════════════════════════════╗")
        print(f"║            Welcome to {self.name:<28}║")
        print("╚═══════════════════════════════════════════════════╝")
        print("  Nav: " + "  |  ".join(self.NAV_CATEGORIES))
        print()

    def print_all_products(self) -> None:
        print(f"  {'Name':<20} {'Category':<12} {'Price':<8} {'Rating':<7} Tag")
        print("  " + "─" * 62)
        for p in self._catalog.values():
            print(f"  {p}")
        print()


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    store = Store("ShopArc  🛍️")

    store.add_product(Product(1, "Wireless Buds",  "Audio",       35.99, "🎧", "sale", 4))
    store.add_product(Product(2, "Smart Watch",    "Wearables",   99.99, "⌚", "new",  5))
    store.add_product(Product(3, "Running Shoes",  "Footwear",    39.99, "👟", "sale", 4))
    store.add_product(Product(4, "Desk Lamp",      "Home",        13.99, "💡", "",     4))
    store.add_product(Product(5, "Mechanical KB",  "Accessories", 64.99, "⌨️", "new",  5))
    store.add_product(Product(6, "Yoga Mat",       "Fitness",     10.99, "🧘", "sale", 4))

    store.print_header()
    print("  ── All Products ──────────────────────────────────")
    store.print_all_products()

    print("  ── On Sale ───────────────────────────────────────")
    for p in store.get_by_tag("sale"):
        print(f"  {p.name:<20}  ${p.price:.2f}")
    print()

    print("  ── Shopping Session ──────────────────────────────")
    cart = store.new_cart()
    cart.add_item(1)    # Wireless Buds
    cart.add_item(2)    # Smart Watch
    cart.add_item(1)    # Wireless Buds again → qty 2
    cart.add_item(5)    # Mechanical KB
    cart.remove_item(2) # changed mind on Watch
    print()

    cart.print_receipt()

    grand_total = cart.subtotal * 1.08
    print(f"\n  ✔  Order placed! ${grand_total:.2f} charged. Thank you for shopping at ShopArc!")


if __name__ == "__main__":
    main()