from abc import ABC, abstractmethod

class IRegistration(ABC):
    @abstractmethod
    def validate_data(self):
        pass

    @abstractmethod
    def save_to_database(self):
        pass

    @abstractmethod
    def send_email(self):
        pass

class CustomerRegistration(IRegistration):
    def validate_data(self):
        print("Validating CPF and email.")

    def save_to_database(self):
        print("Saving customer to the database.")

    def send_email(self):
        print("Sending email to the customer.")

class ProductRegistration(IRegistration):
    def validate_data(self):
        print("Validating product price.")

    def save_to_database(self):
        print("Saving product to the database.")

    def send_email(self):
        raise NotImplementedError("Products do not have emails!")
