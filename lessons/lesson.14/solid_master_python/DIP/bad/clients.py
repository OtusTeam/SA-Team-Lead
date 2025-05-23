import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from datetime import datetime


class Client:
    def __init__(self, client_id, name, email, cpf, registration_date):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.cpf = cpf
        self.registration_date = registration_date

    def is_valid(self):
        return EmailService.is_valid(self.email) and CPFService.is_valid(self.cpf)


class CPFService:
    @staticmethod
    def is_valid(cpf):
        return len(cpf) == 11


class EmailService:
    @staticmethod
    def is_valid(email):
        return '@' in email

    @staticmethod
    def send(from_email, to_email, subject, message):
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP('smtp.google.com', 25) as server:
            server.sendmail(from_email, to_email, msg.as_string())


class ClientRepository:
    def add_client(self, client):
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        query = '''INSERT INTO CLIENT (NAME, EMAIL, CPF, REGISTRATION_DATE) 
                   VALUES (?, ?, ?, ?)'''
        cursor.execute(query, (client.name, client.email, client.cpf, client.registration_date))

        conn.commit()
        conn.close()


class ClientService:
    def add_client(self, client):
        if not client.is_valid():
            return "Invalid data"

        repo = ClientRepository()
        repo.add_client(client)

        EmailService.send('company@company.com', client.email, 'Welcome', 'Congratulations, you are registered')

        return "Client successfully registered"
