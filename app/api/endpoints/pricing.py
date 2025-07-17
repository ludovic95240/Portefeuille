from fastapi import APIRouter, Depends, HTTPException
from datetime import date
from sqlalchemy.orm import Session
from typing import List

from app.db.session import get_db
from app.schemas.historique_prix import HistoriquePrixOut
from app.services.pricing import fetch_and_store_history, get_history

router = APIRouter(prefix="/pricing", tags=["Historique"])

@router.post("/fetch/{ticker}")
def fetch_range(
    ticker: str,
    start: date,
    end: date,
    db: Session = Depends(get_db)
):
    count = fetch_and_store_history(db, ticker, start, end)
    return {"fetched_rows": count}

@router.get("/history/{ticker}", response_model=List[HistoriquePrixOut])
def read_history(
    ticker: str,
    start: date,
    end: date,
    db: Session = Depends(get_db)
):
    rows = get_history(db, ticker, start, end)
    return rows
