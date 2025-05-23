import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import sqlite3
from abc import ABC, abstractmethod


class ICPFService(ABC):
    @abstractmethod
    def is_valid(self, cpf: str) -> bool:
        pass


class IEmailService(ABC):
    @abstractmethod
    def is_valid(self, email: str) -> bool:
        pass

    @abstractmethod
    def send(self, from_email: str, to_email: str, subject: str, message: str):
        pass


class IClientRepository(ABC):
    @abstractmethod
    def add_client(self, client):
        pass


class Client:
    def __init__(self, cpf_service: ICPFService, email_service: IEmailService, client_id, name, email, cpf,
                 registration_date):
        self.cpf_service = cpf_service
        self.email_service = email_service
        self.client_id = client_id
        self.name = name
        self.email = email
        self.cpf = cpf
        self.registration_date = registration_date

    def is_valid(self) -> bool:
        return self.email_service.is_valid(self.email) and self.cpf_service.is_valid(self.cpf)


class CPFService(ICPFService):
    def is_valid(self, cpf: str) -> bool:
        return len(cpf) == 11


class EmailService(IEmailService):
    def is_valid(self, email: str) -> bool:
        return '@' in email

    def send(self, from_email: str, to_email: str, subject: str, message: str):
        msg = MIMEMultipart()
        msg['From'] = from_email
        msg['To'] = to_email
        msg['Subject'] = subject

        msg.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP('smtp.google.com', 25) as server:
            server.sendmail(from_email, to_email, msg.as_string())


class ClientRepository(IClientRepository):
    def add_client(self, client: Client):
        conn = sqlite3.connect('my_database.db')
        cursor = conn.cursor()

        query = '''INSERT INTO CLIENT (NAME, EMAIL, CPF, REGISTRATION_DATE) 
                   VALUES (?, ?, ?, ?)'''
        cursor.execute(query, (client.name, client.email, client.cpf, client.registration_date))

        conn.commit()
        conn.close()


class ClientService:
    def __init__(self, email_service: IEmailService, client_repository: IClientRepository):
        self.email_service = email_service
        self.client_repository = client_repository

    def add_client(self, client: Client) -> str:
        if not client.is_valid():
            return "Invalid data"

        self.client_repository.add_client(client)
        self.email_service.send('company@company.com', client.email, 'Welcome', 'Congratulations, you are registered')

        return "Client successfully registered"
