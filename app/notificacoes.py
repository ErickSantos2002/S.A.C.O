# notificacoes.py
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_REMETENTE = "seuemail@gmail.com"
SENHA_APP = "sua_senha_de_aplicativo"

def enviar_email(destinatario, assunto, corpo):
    msg = MIMEMultipart()
    msg["From"] = EMAIL_REMETENTE
    msg["To"] = destinatario
    msg["Subject"] = assunto

    msg.attach(MIMEText(corpo, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_REMETENTE, SENHA_APP)
        server.send_message(msg)