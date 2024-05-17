from abc import ABC, abstractmethod

class InvoicePersistence(ABC):
    @abstractmethod
    def save(self, invoice):
        pass

class FilePersistence(InvoicePersistence):
    def save(self, invoice):
        # Save the invoice to a file
        print("Saving invoice to file:", invoice)

class DatabasePersistence(InvoicePersistence):
    def save(self, invoice):
        # Save the invoice to a database
        print("Saving invoice to database:", invoice)

class PersistenceManager:
    def __init__(self, persistence):
        self.persistence = persistence

    def save_invoice(self, invoice):
        self.persistence.save(invoice)

# Usage example
invoice = "Sample Invoice"
file_persistence = FilePersistence()
db_persistence = DatabasePersistence()

pm = PersistenceManager(file_persistence)
pm.save_invoice(invoice)  # Saving invoice to file: Sample Invoice

pm = PersistenceManager(db_persistence)
pm.save_invoice(invoice)  # Saving invoice to database: Sample Invoice