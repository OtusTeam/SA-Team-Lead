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

    def add_client(self):
        # Валидация
        if "@" not in self.email:
            return "Invalid email"

        if len(self.cpf) != 11:
            return "Invalid CPF"

        # Сохранение в БД
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO client (name, email, cpf, registration_date) VALUES (?, ?, ?, ?)",
            (self.name, self.email, self.cpf, self.registration_date),
        )

        conn.commit()
        conn.close()

        # Отправка Email
        msg = MIMEText("Congratulations! You are registered.")
        msg["Subject"] = "Welcome"
        msg["From"] = "company@company.com"
        msg["To"] = self.email

        smtp = smtplib.SMTP("smtp.google.com", 25)
        smtp.sendmail("company@company.com", [self.email], msg.as_string())
        smtp.quit()

        return "Client registered successfully!"

# Пример использования
client = Client(1, "John Doe", "john@example.com", "12345678901", "2024-03-12")
print(client.add_client())
