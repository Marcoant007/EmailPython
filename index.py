import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

token = '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'
sender = "marcoantnovo@gmail.com"
receiver = input('Informe o seu email: ');
subject = input("Informe o assunto do email: ");

message = Mail(
    from_email=receiver,
    to_emails=sender,
    subject="Oi",
    plain_text_content='Funcionando certinho ? (internet ta lenta né ?)',
    html_content='Funcionando certinho ?')

sg = SendGridAPIClient(token)
response = sg.send(message)
print("Email enviado")

