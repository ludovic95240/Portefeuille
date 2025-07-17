# frontend/dashboard.py
import streamlit as st
import pandas as pd
import requests

st.set_page_config(page_title="💼 Portefeuille Boursier", layout="wide")
st.title("📊 Mon Portefeuille d'Actions")

# === Paramètres utilisateur ===
token = st.text_input("🔐 Token d'accès", type="password")
url_api = "http://127.0.0.1:8000/portefeuille/"

if token:
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url_api, headers=headers)

    if response.status_code == 200:
        data = response.json()
        df = pd.DataFrame(data)

        df['prix_total'] = df['prix_achat'] * df['quantite']
        df['gain_net_pct'] = df['gain_net'] / df['prix_total'] * 100

        st.dataframe(df[[
            'ticker', 'nom', 'quantite', 'prix_achat', 'current_price',
            'gain_eur', 'swap_total', 'gain_net', 'gain_net_pct'
        ]].round(2).sort_values(by='gain_net_pct', ascending=False))

        st.bar_chart(df.set_index('ticker')['gain_net'])

        with st.expander("🔁 Données brutes"):
            st.dataframe(df)
    else:
        st.error(f"Erreur API : {response.status_code} - {response.text}")
else:
    st.warning("Veuillez entrer un token JWT valide pour accéder à vos données.")
