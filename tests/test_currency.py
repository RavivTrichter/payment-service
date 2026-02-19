from app.currency import convert_currency

def test_basic_conversion():
    assert convert_currency(100, "USD", "EUR") == 92.0

def test_rounding():
    result = convert_currency(99.995, "USD", "EUR")
    assert isinstance(result, float)
