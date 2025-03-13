import streamlit as st
import smtplib
from email.mime.text import MIMEText

def send_email(user_email, responses):
    EMAIL_SENDER = "votre_email@gmail.com"
    EMAIL_PASSWORD = "votre_mot_de_passe"
    EMAIL_RECEIVER = "destinataire_email@gmail.com"
    
    subject = "Réponses du formulaire"
    body = f"Adresse e-mail de l'utilisateur : {user_email}\n\n"
    body += "\n".join([f"{q}: {r}" for q, r in responses.items()])
    
    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER
    
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, msg.as_string())
        return "E-mail envoyé avec succès !"
    except Exception as e:
        return f"Erreur lors de l'envoi de l'e-mail : {e}"

# Interface Streamlit
st.title("Formulaire de validation")

user_email = st.text_input("Votre adresse e-mail", "")

questions = [
    "Avez-vous bien compris les consignes ?",
    "Le matériel est-il prêt ?",
    "L'équipe est-elle complète ?",
    "Les conditions météo sont-elles favorables ?"
]

responses = {}
for question in questions:
    responses[question] = st.radio(question, ["Oui", "Non"], index=0)

if st.button("Envoyer"):
    if user_email:
        result = send_email(user_email, responses)
        st.success(result)
    else:
        st.error("Veuillez entrer votre adresse e-mail.")