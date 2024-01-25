from flask import Flask, render_template, request
import smtplib
from email.message import EmailMessage

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    subject = request.form['subject']
    to = request.form['to']
    content = request.form['content']

    EMAIL_ADDRESS = ""
    EMAIL_PASSWORD = ""

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = to
    msg.set_content(content)

    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            for _ in range(4):  # Enviar o e-mail 4 vezes
                smtp.send_message(msg)
        return 'Email enviado com sucesso 4 vezes!'
    except Exception as e:
        return f'Erro ao enviar e-mail: {e}'

if __name__ == '__main__':
    app.run(debug=True)
