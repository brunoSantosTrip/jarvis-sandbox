"""Toy pricing helpers used to exercise the Jarvis propose/approve flow."""


def apply_discount(price_cents: int, percent_off: int) -> int:
    """Return the price after a percentage discount, in whole cents."""
    return price_cents - (price_cents * percent_off // 100)


def total_with_tax(price_cents: int, tax_percent: int) -> int:
    """Return the price with tax added, in whole cents."""
    tax_percent = max(tax_percent, 0)
    return price_cents + (price_cents * tax_percent // 100)
