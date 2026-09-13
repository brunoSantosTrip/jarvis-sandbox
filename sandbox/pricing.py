"""Toy pricing helpers used to exercise the Jarvis propose/approve flow."""


def apply_discount(price_cents: int, percent_off: int) -> int:
    """Return the price after a percentage discount, in whole cents.

    ``percent_off`` is clamped into ``[0, 100]`` so the result is never
    negative and never larger than ``price_cents``.
    """
    percent_off = max(0, min(100, percent_off))
    return price_cents - (price_cents * percent_off // 100)


def total_with_tax(price_cents: int, tax_percent: int) -> int:
    """Return the price with tax added, in whole cents."""
    return price_cents + (price_cents * tax_percent // 100)
