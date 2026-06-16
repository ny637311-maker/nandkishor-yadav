from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass

    @abstractmethod
    def receipt(self):
        pass



class GPay(Payment):
    def pay(self):
        print("Payment done using GPay")

    def receipt(self):
        print("GPay receipt generated")



class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card")

    def receipt(self):
        print("Credit Card receipt generated")



g1 = GPay()
c1 = CreditCard()

print("GPay:")
g1.pay()

g1.receipt()

print("\nCredit Card:")
c1.pay()
c1.receipt()