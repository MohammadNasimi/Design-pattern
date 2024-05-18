from abc import ABC, abstractmethod

# Bad Design: Large Interface
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

    @abstractmethod
    def scan(self, document):
        pass

    @abstractmethod
    def fax(self, document):
        pass

class SimplePrinter(Printer):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

    def fax(self, document):
        # Not supported by SimplePrinter
        raise NotImplementedError("Faxing is not supported by this printer.")

# Good Design: Segregated Interfaces
class Printer(ABC):
    @abstractmethod
    def print(self, document):
        pass

class Scanner(ABC):
    @abstractmethod
    def scan(self, document):
        pass

class FaxMachine(ABC):
    @abstractmethod
    def fax(self, document):
        pass

class SimplePrinter(Printer, Scanner):
    def print(self, document):
        print(f"Printing: {document}")

    def scan(self, document):
        print(f"Scanning: {document}")

# Usage
document = "Sample Document"
printer = SimplePrinter()
printer.print(document)
printer.scan(document)