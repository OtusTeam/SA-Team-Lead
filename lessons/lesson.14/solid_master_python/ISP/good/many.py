from abc import ABC, abstractmethod

# Define separate interfaces
class ICustomerRegistration(ABC):
    @abstractmethod
    def validate_data(self):
        pass

    @abstractmethod
    def save_to_database(self):
        pass

    @abstractmethod
    def send_email(self):
        pass

class IProductRegistration(ABC):
    @abstractmethod
    def validate_data(self):
        pass

    @abstractmethod
    def save_to_database(self):
        pass

# Implementing the customer registration
class CustomerRegistration(ICustomerRegistration):
    def validate_data(self):
        print("Validating CPF and email.")

    def save_to_database(self):
        print("Saving customer to the database.")

    def send_email(self):
        print("Sending email to the customer.")

# Implementing the product registration
class ProductRegistration(IProductRegistration):
    def validate_data(self):
        print("Validating product price.")

    def save_to_database(self):
        print("Saving product to the database.")
