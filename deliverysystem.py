class Customer:
    def delivery_charge(self):
        print("charge is 50 rs")
class PrimeCustomer:
    def delivery_charge(self):
        print("charge is 30 rs with discount of 20 rs")
primeCustomer=PrimeCustomer()
primeCustomer.delivery_charge()        
        