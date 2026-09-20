"""Toy pricing helpers used to exercise the Jarvis propose/approve flow."""


def apply_discount(price_cents: int, percent_off: int) -> int:
    """Return the price after a percentage discount, in whole cents."""
    return price_cents - (price_cents * percent_off // 100)


def total_with_tax(price_cents: int, tax_percent: int) -> int:
    """Return the price with tax added, in whole cents."""
    return price_cents + (price_cents * tax_percent // 100)


def split_across(total_cents: int, n: int) -> list[int]:
    """Split total_cents across n travellers so the parts sum to total_cents
    and differ by at most one cent. The first `remainder` travellers get the
    extra cent."""
    base, remainder = divmod(total_cents, n)
    return [base + 1] * remainder + [base] * (n - remainder)
