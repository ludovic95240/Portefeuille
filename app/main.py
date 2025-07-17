from fastapi import FastAPI
from app.api.endpoints import auth, portefeuille
from app.db.session import engine
from app.models import user, action
from app.models import historique_prix




app = FastAPI()


app.include_router(auth.router, prefix="/auth", tags=["Authentification"])
app.include_router(portefeuille.router, prefix="/portefeuille", tags=["Portefeuille"])

# Puis crée les tables
user.Base.metadata.create_all(bind=engine)
action.Base.metadata.create_all(bind=engine)
historique_prix.Base.metadata.create_all(bind=engine)
@app.get("/")
def root():
    return {"msg": "Hello depuis ta base API"}
