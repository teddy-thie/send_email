from flask import Flask, request, jsonify, render_template
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

app = Flask(__name__)

def send_test_mail(body):
    sender_email = "ted.thie@outlook.com"
    receiver_email = "ted.thie@outlook.com"

    msg = MIMEMultipart()
    msg['Subject'] = '[Email Test]'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    msgText = MIMEText('<b>%s</b>' % (body), 'html')
    msg.attach(msgText)
        
    pdf = MIMEApplication(open("CV.pdf", 'rb').read())
    pdf.add_header('Content-Disposition', 'attachment', filename= "CV.pdf")
    msg.attach(pdf)

    try:
        with smtplib.SMTP('smtp.office365.com', 587) as smtpObj:
            smtpObj.ehlo()
            smtpObj.starttls()
            smtpObj.login("ted.thie@outlook.com", "Tedthie69")
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(e)
        
@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    send_test_mail("TEST EMAIL SUCCESSFUL")
    app.run(port=5000)