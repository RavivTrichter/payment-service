from fastapi import FastAPI
from app.currency import convert_currency

app = FastAPI(title="Payment Service", version="3.8.0")

@app.post("/api/v1/payments/convert")
async def convert(amount: float, from_currency: str, to_currency: str):
    converted = convert_currency(amount, from_currency, to_currency)
    return {"original": amount, "converted": converted, "from": from_currency, "to": to_currency}
