"""Toy pricing helpers used to exercise the Jarvis propose/approve flow."""


def apply_discount(price_cents: int, percent_off: int) -> int:
    """Return the price after a percentage discount, in whole cents."""
    return price_cents - (price_cents * percent_off // 100)


def total_with_tax(price_cents: int, tax_percent: int) -> int:
    """Return the price with tax added, in whole cents."""
    return price_cents + (price_cents * tax_percent // 100)


def discounted_total_with_tax(
    price_cents: int, percent_off: int, tax_percent: int
) -> int:
    """Return the price after discount and tax, in whole cents.

    The discount is applied first, then tax is charged on the discounted
    amount. That is the order a customer sees on a receipt and the amount
    tax is actually charged on, so callers should use this helper rather
    than composing ``apply_discount`` and ``total_with_tax`` themselves --
    the two possible orders can disagree by a cent once rounding lands
    differently.

    Delegates to ``apply_discount`` and ``total_with_tax`` so their
    rounding behaviour applies here unchanged.
    """
    return total_with_tax(apply_discount(price_cents, percent_off), tax_percent)
