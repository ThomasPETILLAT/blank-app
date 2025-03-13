import streamlit as st
# from fpdf import FPDF
import smtplib
from email.message import EmailMessage


# Titre de l'application
st.title("Questionnaire de Satisfaction Client")

# Formulaire basé sur le PDF
nom = st.text_input("Nom")
email = st.text_input("Email")
commentaires = st.text_area("Commentaires")
satisfaction = st.selectbox("Niveau de satisfaction", ["Très satisfait", "Satisfait", "Neutre", "Insatisfait", "Très insatisfait"])

# Génération du PDF
def generate_pdf(nom, email, commentaires, satisfaction):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Questionnaire de Satisfaction Client", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, f"Nom: {nom}", ln=True)
    pdf.cell(200, 10, f"Email: {email}", ln=True)
    pdf.cell(200, 10, f"Satisfaction: {satisfaction}", ln=True)
    pdf.multi_cell(200, 10, f"Commentaires: {commentaires}")
    file_path = "/tmp/formulaire.pdf"
    pdf.output(file_path)
    return file_path

# Envoi de l'email
def send_email(pdf_path, user_email):
    msg = EmailMessage()
    msg['Subject'] = "Formulaire de Satisfaction"
    msg['From'] = user_email
    msg['To'] = "envoieformulairerb@gmail.com"
    msg.set_content("Veuillez trouver ci-joint le formulaire de satisfaction complété.")
    
    with open(pdf_path, "rb") as f:
        msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename="formulaire.pdf")
    
    with smtplib.SMTP("smtp.example.com", 587) as server:
        server.starttls()
        server.login("votre_email@example.com", "votre_mot_de_passe")
        server.send_message(msg)
    
    st.success("Formulaire envoyé avec succès !")

# Bouton de soumission
if st.button("Envoyer"):
    if nom and email:
        pdf_path = generate_pdf(nom, email, commentaires, satisfaction)
        send_email(pdf_path, email)
    else:
        st.error("Veuillez remplir tous les champs obligatoires.")
