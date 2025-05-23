import sqlite3
import smtplib
from email.mime.text import MIMEText


class Client:
    def __init__(self, client_id, name, email, cpf, registration_date):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.cpf = cpf
        self.registration_date = registration_date

    def is_valid(self):
        return EmailService.is_valid(self.email) and CPFService.is_valid(self.cpf)


class ClientRepository:
    @staticmethod
    def add_client(client):
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO client (name, email, cpf, registration_date) VALUES (?, ?, ?, ?)",
            (client.name, client.email, client.cpf, client.registration_date),
        )

        conn.commit()
        conn.close()


class ClientService:
    @staticmethod
    def add_client(client):
        if not client.is_valid():
            return "Invalid data"

        ClientRepository.add_client(client)

        EmailService.send(
            "company@company.com",
            client.email,
            "Welcome",
            "Congratulations! You are registered.",
        )

        return "Client registered successfully!"


class CPFService:
    @staticmethod
    def is_valid(cpf):
        return len(cpf) == 11


class EmailService:
    @staticmethod
    def is_valid(email):
        return "@" in email

    @staticmethod
    def send(sender, recipient, subject, message):
        msg = MIMEText(message)
        msg["Subject"] = subject
        msg["From"] = sender
        msg["To"] = recipient

        smtp = smtplib.SMTP("smtp.google.com", 25)
        smtp.sendmail(sender, [recipient], msg.as_string())
        smtp.quit()


# Example usage
client = Client(1, "John Doe", "john@example.com", "12345678901", "2024-03-12")
print(ClientService.add_client(client))
