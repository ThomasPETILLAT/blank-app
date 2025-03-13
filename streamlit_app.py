import streamlit as st
import smtplib
from email.message import EmailMessage




razel_bec_url = "https://razel-bec.fayat.com/"
image_path = "/workspaces/blank-app/Logo_Razel-Bec.jpg"

# Afficher l'image avec un texte cliquable en dessous
st.image(image_path, use_container_width=True)
st.markdown(f"[Cliquez ici pour accéder à Razel-Bec]({razel_bec_url})")






# Titre et description
titre = "Questionnaire de satisfaction client"
description = """
L'entreprise RAZEL-BEC recherche une amélioration continue de ses prestations pour fournir des produits de qualité, 
tout en respectant les principes de santé, de sécurité, et de protection de l'environnement.
Nous vous remercions d'avance du temps que vous consacrerez à ce questionnaire. 
Vos réponses nous permettront d'améliorer notre démarche pour mieux répondre à vos attentes.
"""

st.title(titre)
st.write(description)

# Formulaire
tnom = st.text_input("Nom et Prénom")
entreprise = st.text_input("Entreprise")

satisfaction_chantier = st.slider("Satisfaction sur le chantier", 1, 5, 3)

respect_exigences = st.radio("Respect des exigences et du cahier des charges", 
    ["Pas du tout satisfait", "Peu satisfait", "Satisfait", "Très satisfait", "Non concerné"])
commentaire_exigences = st.text_area("Commentaire sur le respect des exigences")

respect_delais = st.radio("Respect des délais", 
    ["Pas du tout satisfait", "Peu satisfait", "Satisfait", "Très satisfait", "Non concerné"])
commentaire_delais = st.text_area("Commentaire sur le respect des délais")

qualite_offre = st.radio("Qualité de l'offre proposée", 
    ["Pas du tout satisfait", "Peu satisfait", "Satisfait", "Très satisfait", "Non concerné"])
commentaire_offre = st.text_area("Commentaire sur la qualité de l'offre")

# Conclusion
commentaires_generaux = st.text_area("Commentaires et appréciation générale")
attentes = st.text_area("Vos attentes")

# Email utilisateur
email_utilisateur = st.text_input("Votre adresse e-mail (pour recevoir une copie)")

def send_email():
    msg = EmailMessage()
    msg['Subject'] = "Réponse au Questionnaire de Satisfaction"
    msg['From'] = email_utilisateur if email_utilisateur else "no-reply@razel-bec.com"
    msg['To'] = "envoieformulairerb@gmail.com"
    
    contenu = f"""
    Nom et Prénom: {tnom}
    Entreprise: {entreprise}
    Satisfaction sur le chantier: {satisfaction_chantier}/5
    Respect des exigences et cahier des charges: {respect_exigences}
    Commentaire: {commentaire_exigences}
    Respect des délais: {respect_delais}
    Commentaire: {commentaire_delais}
    Qualité de l'offre proposée: {qualite_offre}
    Commentaire: {commentaire_offre}
    Commentaires et appréciation générale: {commentaires_generaux}
    Vos attentes: {attentes}
    """
    msg.set_content(contenu)
    
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login("ton_email@gmail.com", "TON_MOT_DE_PASSE_APPLICATION")
            server.send_message(msg)
        st.success("✅ Questionnaire envoyé avec succès !")
    except Exception as e:
        st.error(f"❌ Erreur lors de l'envoi : {e}")

# Bouton d'envoi
if st.button("Envoyer le questionnaire"):
    if tnom and entreprise:
        send_email()
    else:
        st.error("⚠ Veuillez remplir tous les champs obligatoires.")
