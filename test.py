from flask import Flask, request, jsonify, render_template, flash
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication

app = Flask(__name__)

def send_test_mail(email, body):
    sender_email = "ted.thie@outlook.com"
    receiver_email = email

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
            print(smtpObj.starttls())
            print(smtpObj.login("ted.thie@outlook.com", "Tedthie69"))
            smtpObj.sendmail(sender_email, receiver_email, msg.as_string())

        return True
    except Exception as e:
        print(e)
        return False
        
@app.route('/')
def index():
    return render_template("index.html")


@app.route('/send', methods=['POST'])
def send_mail():
    email = request.form.get('email')

    print('sending mail - ', email)
    res = send_test_mail(email, "TEST EMAIL SUCCESSFUL")

    if res:
        result = {
            'code': 'Success',
            'msg': 'Email Sent Successfully'
        }
    else:
        result = {
            'code': 'Failed',
            'msg': 'Email Could not be sent, please check email and try again.'
        }

    return render_template("result.html", result=result)


if __name__ == "__main__":
    app.run(port=5000)