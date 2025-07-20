from fastapi import APIRouter, HTTPException, Query
from app.services.var_service import compute_var

router = APIRouter()

@router.get("/{ticker}")
def get_var(
    ticker: str,
    sims: int = Query(10000, ge=1000, le=100000),
    horizon: int = Query(1, ge=1, le=30),
    cl: float = Query(0.95, gt=0.5, lt=1.0)
):
    """
    Calcule la Value at Risk (VaR) pour un ticker donné en utilisant Monte Carlo.
    - **ticker**: symbole boursier
    - **sims**: nombre de simulations
    - **horizon**: nombre de jours à simuler
    - **cl**: niveau de confiance (0 < cl < 1)
    """
    try:
        result = compute_var(
            ticker,
            num_simulations=sims,
            horizon_days=horizon,
            confidence_level=cl
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))