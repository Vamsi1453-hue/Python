class Owner:
    def __init__(self, owner_name):
        self.owner_name = owner_name


class Pet:
    def __init__(self, pet_name):
        self.pet_name = pet_name


class Appointment:
    def __init__(self, service, charge):
        self.service = service
        self.charge = charge

    def generate_receipt(self, owner, pet):
        print("=" * 50)
        print("            SERVICE RECEIPT")
        print("=" * 50)

        print(f"\nOwner Name : {owner.owner_name}")
        print(f"Pet Name   : {pet.pet_name}")

        print(f"\nService    : {self.service}")
        print(f"\nAmount     : ₹{self.charge}")

        print("\n" + "=" * 50)


owner = Owner("Ethan")
pet = Pet("Bruno")

appointment = Appointment("Grooming", 800)
appointment.generate_receipt(owner, pet)