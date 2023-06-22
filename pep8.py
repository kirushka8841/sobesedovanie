# Мы устроились на новую работу. Бывший сотрудник начал разрабатывать модуль для работы с почтой, но не успел доделать его. Код рабочий. Нужно только провести рефакторинг кода.

# 1. Создать класс для работы с почтой;
# 2. Создать методы для отправки и получения писем;
# 3. Убрать "захардкоженный" код. Все значения должны определяться как аттрибуты класса, либо аргументы методов;
# 4. Переменные должны быть названы по стандарту PEP8;
# 5. Весь остальной код должен соответствовать стандарту PEP8;
# 6. Класс должен инициализироваться в конструкции.


import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class Mail:
    def __init__(self, smtpaddress: str, imapaddress: str, senderemail: str, senderpassword: str):
        self.smtpaddress = smtpaddress
        self.imapaddress = imapaddress
        self.senderemail = senderemail
        self.senderpassword = senderpassword

    def send_email(self, recipients: list, subject: str, message: str):
        msg = MIMEMultipart()
        msg['From'] = self.senderemail
        msg['To'] = ', '.join(recipients)
        msg['Subject'] = subject
        msg.attach(MIMEText(message))

        ms = smtplib.SMTP(self.smtpaddress, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()
        ms.login(self.senderemail, self.senderpassword)
        ms.sendmail(self.senderemail, recipients, msg.asstring())
        ms.quit()

    def receive_email(self, header: str) -> str:
        mail = imaplib.IMAP4_SSL(self.imapaddress)
        mail.login(self.senderemail, self.senderpassword)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % header if header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_string(raw_email)
        mail.logout()  
        return email_message

if __name__ == '__main__':
    smtp_address = "smtp.gmail.com"
    imap_address = "imap.gmail.com"
    sender_email = 'login@gmail.com'
    sender_password = 'qwerty'
    recipients = ['email1@example.com', 'email2@example.com']
    subject = 'Subject'
    message = 'Message'
    header = None

    mail = Mail(smtp_address, imap_address, sender_email, sender_password)
    mail.send_email(recipients, subject, message)
    received_email = mail.receive_email(header)




