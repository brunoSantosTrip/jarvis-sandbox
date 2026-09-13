from sandbox.pricing import apply_discount, total_with_tax


def test_apply_discount_halves_the_price():
    assert apply_discount(1000, 50) == 500


def test_apply_discount_of_nothing_changes_nothing():
    assert apply_discount(1000, 0) == 1000


def test_apply_discount_over_one_hundred_percent_clamps_to_free():
    assert apply_discount(1000, 150) == 0


def test_apply_discount_negative_percent_clamps_to_no_discount():
    assert apply_discount(1000, -10) == 1000


def test_total_with_tax_adds_the_percentage():
    assert total_with_tax(1000, 10) == 1100
