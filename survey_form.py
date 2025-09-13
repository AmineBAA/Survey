import streamlit as st
import pandas as pd
import os

# Nom du fichier pour stocker les réponses
FICHIER = "reponses_sondage.csv"

st.title("📋 Questionnaire Client Banque")

# Charger le fichier existant ou créer une base vide
if os.path.exists(FICHIER):
    df = pd.read_csv(FICHIER)
else:
    df = pd.DataFrame(columns=["Nom", "Age", "Q1", "Q2", "Q3"])

# Formulaire
with st.form("sondage_formulaire", clear_on_submit=True):  # <- clear permet de vider après soumission
    nom = st.text_input("Nom et prénom")
    age = st.number_input("Âge", min_value=18, max_value=100)
    
    q1 = st.radio("Utilisez-vous les services digitaux de la banque ?", ["Oui", "Non"])
    
    # Question conditionnelle
    if q1 == "Oui":
        q2 = st.selectbox("Quels services utilisez-vous ?", ["Mobile Banking", "E-banking", "Paiement par carte"])
    else:
        q2 = st.text_input("Pourquoi vous n’utilisez pas les services digitaux ?")
    
    q3 = st.slider("Votre satisfaction globale (0=faible, 10=très forte)", 0, 10, 5)
    
    submitted = st.form_submit_button("✅ Envoyer")

# Sauvegarde des réponses
if submitted:
    nouvelle_ligne = {"Nom": nom, "Age": age, "Q1": q1, "Q2": q2, "Q3": q3}
    df = pd.concat([df, pd.DataFrame([nouvelle_ligne])], ignore_index=True)
    df.to_csv(FICHIER, index=False)
    st.success("Merci ! Votre réponse a bien été enregistrée ✅")

# Affichage en temps réel des réponses déjà collectées
st.subheader("📊 Réponses enregistrées")
st.dataframe(df)
