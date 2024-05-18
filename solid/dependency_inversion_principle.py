from abc import ABC, abstractmethod

# High-level Module
class PaymentProcessor:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount):
        self.payment_gateway.pay(amount)

# Low-level Modules
class PayPalGateway:
    def pay(self, amount):
        print(f"Processing payment of ${amount} via PayPal.")

class StripeGateway:
    def pay(self, amount):
        print(f"Processing payment of ${amount} via Stripe.")

# Abstraction/Interface
class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Dependency Injection
paypal_gateway = PayPalGateway()
payment_processor = PaymentProcessor(paypal_gateway)
payment_processor.process_payment(100)

stripe_gateway = StripeGateway()
payment_processor = PaymentProcessor(stripe_gateway)
payment_processor.process_payment(200)