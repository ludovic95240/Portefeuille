from fastapi import APIRouter, HTTPException
from app.services.yfinance_service import fetch_history
from app.services.kpi_service import compute_kpis

router = APIRouter()

@router.get("/{ticker}")
async def get_kpis(ticker: str):
    try:
        df = fetch_history(ticker)
        data = compute_kpis(df["close"])
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))