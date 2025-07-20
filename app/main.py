from fastapi import FastAPI
from app.api.endpoints import quotes, kpis

app = FastAPI(title="Portefeuille SaaS - Prototype")

app.include_router(quotes.router, prefix="/quotes", tags=["Quotes"])
app.include_router(kpis.router, prefix="/kpis", tags=["KPIs"])

@app.get("/")
def root():
    return {"msg": "Portefeuille API opérationnel"}