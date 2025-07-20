from fastapi import APIRouter, HTTPException
from app.services.yfinance_service import fetch_history, fetch_current_price

router = APIRouter()

@router.get("/{ticker}")
def get_quotes(ticker: str):
    try:
        df = fetch_history(ticker)
        return {"history": df.to_dict(orient="list"), "current": fetch_current_price(ticker)}
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))