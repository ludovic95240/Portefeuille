from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.schemas.action import ActionCreate, ActionOut
from app.core.security import get_current_user
from app.db.session import get_db
from app.crud import action
from app.models.user import User
from app.services.yfinance_service import get_current_price
from app.schemas.action import ActionFullOut

router = APIRouter()

@router.post("/", response_model=ActionOut)
def add_action_to_portfolio(
    action_data: ActionCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return action.create_action(db, action_data, current_user.id)

@router.get("/", response_model=List[ActionOut])
def list_user_actions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return action.get_actions_by_user(db, current_user.id)

@router.delete("/{action_id}", response_model=dict)
def remove_action(
    action_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    success = action.delete_action(db, action_id, current_user.id)
    if not success:
        raise HTTPException(status_code=404, detail="Action introuvable")
    return {"message": "Action supprimée"}

@router.get("/", response_model=List[ActionFullOut])
def list_user_actions(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    actions = action.get_actions_by_user(db, current_user.id)
    results = []
    for a in actions:
        current = get_current_price(a.ticker)
        gain_eur = ((current - a.prix_achat) * a.quantite) if current else None
        gain_pct = ((current - a.prix_achat) / a.prix_achat * 100) if current else None

        results.append(ActionFullOut(
            id=a.id,
            ticker=a.ticker,
            nom=a.nom,
            devise=a.devise,
            quantite=a.quantite,
            prix_achat=a.prix_achat,
            current_price=current,
            gain_eur=round(gain_eur, 2) if gain_eur else None,
            gain_percent=round(gain_pct, 2) if gain_pct else None
        ))
    return results
