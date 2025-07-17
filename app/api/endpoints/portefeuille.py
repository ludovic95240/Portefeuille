from datetime import datetime
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.action import ActionCreate, ActionFullOut
from app.core.security import get_current_user
from app.db.session import get_db
from app.crud import action
from app.models.user import User
from app.services.yfinance_service import get_current_price

router = APIRouter()

@router.get("/", response_model=List[ActionFullOut])
def list_user_actions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    actions = action.get_actions_by_user(db, current_user.id)
    results = []
    for a in actions:
        current = get_current_price(a.ticker)
        days_open = (datetime.now().date() - a.date_achat).days if a.date_achat else 0
        swap_total = (a.prix_achat * a.quantite) * (a.swap_rate / 100) * (days_open / 365)

        gain_eur = ((current - a.prix_achat) * a.quantite) if current else None
        gain_pct = ((current - a.prix_achat) / a.prix_achat * 100) if current else None
        gain_net = gain_eur - swap_total if gain_eur else None

        results.append(ActionFullOut(
            id=a.id,
            ticker=a.ticker,
            nom=a.nom,
            devise=a.devise,
            quantite=a.quantite,
            prix_achat=a.prix_achat,
            swap_rate=a.swap_rate,
            date_achat=a.date_achat,
            current_price=round(current, 2) if current else None,
            gain_eur=round(gain_eur, 2) if gain_eur else None,
            gain_percent=round(gain_pct, 2) if gain_pct else None,
            swap_total=round(swap_total, 2),
            gain_net=round(gain_net, 2) if gain_net else None
        ))
    return results
