"""Toy pricing helpers used to exercise the Jarvis propose/approve flow."""


def apply_discount(price_cents: int, percent_off: int) -> int:
    """Return the price after a percentage discount, in whole cents.

    Fractional cents round in the customer's favour: the discount is
    ceilinged so the final price is floored. e.g. a 10% discount on 999
    cents leaves 899, not 900.
    """
    return price_cents - -(-price_cents * percent_off // 100)


def total_with_tax(price_cents: int, tax_percent: int) -> int:
    """Return the price with tax added, in whole cents.

    Fractional cents round in the tax authority's favour: the tax is
    ceilinged so the merchant never collects less than the stated rate.
    """
    return price_cents + -(-price_cents * tax_percent // 100)
