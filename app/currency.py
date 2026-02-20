"""Currency conversion module."""
from decimal import Decimal, ROUND_HALF_EVEN

EXCHANGE_RATES = {
    ("USD", "EUR"): Decimal("0.92"),
    ("USD", "GBP"): Decimal("0.79"),
    ("EUR", "USD"): Decimal("1.09"),
    ("GBP", "USD"): Decimal("1.27"),
}

def convert_currency(amount: float, from_curr: str, to_curr: str) -> float:
    """Convert currency amount using banker's rounding (round half to even).
    
    This ensures consistent rounding behavior for financial calculations,
    eliminating the 1-cent discrepancies seen with standard rounding.
    """
    rate = EXCHANGE_RATES.get((from_curr, to_curr), Decimal("1.0"))
    result = Decimal(str(amount)) * rate
    rounded = result.quantize(Decimal("0.01"), rounding=ROUND_HALF_EVEN)
    return float(rounded)
