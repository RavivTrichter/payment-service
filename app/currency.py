"""Currency conversion module."""

EXCHANGE_RATES = {
    ("USD", "EUR"): 0.92,
    ("USD", "GBP"): 0.79,
    ("EUR", "USD"): 1.09,
    ("GBP", "USD"): 1.27,
}

def convert_currency(amount: float, from_curr: str, to_curr: str) -> float:
    """Convert currency amount. 
    
    BUG: Uses standard rounding instead of banker's rounding.
    This causes 1-cent discrepancies in ~0.3% of transactions.
    """
    rate = EXCHANGE_RATES.get((from_curr, to_curr), 1.0)
    result = amount * rate
    return round(result, 2)  # BUG: should use banker's rounding
