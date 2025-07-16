from fastapi import FastAPI
from app.db.session import engine
from app.api.endpoints import auth, portefeuille
from app.models import user, action

# Étape 1 : créer l'instance FastAPI
app = FastAPI(title="SAAS Bourse")

# Étape 2 : inclure les routers
app.include_router(auth.router, prefix="/auth", tags=["Authentification"])
app.include_router(portefeuille.router, prefix="/portefeuille", tags=["Portefeuille"])


# Étape 3 : créer les tables
user.Base.metadata.create_all(bind=engine)
action.Base.metadata.create_all(bind=engine)

# Étape 4 : route racine
@app.get("/")
def root():
    return {"msg": "Hello depuis ta base API"}

print(app.routes)
