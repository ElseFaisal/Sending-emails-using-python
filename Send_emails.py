import smtplib
import email.mime.text as emt
from email.header import Header

smtp_server = 'smtp.gmail.com'
smtp_port = 587

smtp_username = '' # Your email
smtp_password = '' # Your app generated password

from_email = '' # Your email
to_emails = [] # Emails you want to send

msg = emt.MIMEText("", _charset = "UTF-8") # Body message (Note: if you don't want it in arabic language, just remove the second parameter)

msg['Subject'] = Header("", "UTF-8") # # Subject (Note: if you don't want it in arabic language, just remove the second parameter)



with smtplib.SMTP(smtp_server, smtp_port) as smtp:
    smtp.starttls()
    smtp.login(smtp_username, smtp_password)
    for e in to_emails:
        smtp.sendmail(from_email, e, msg.as_string())

