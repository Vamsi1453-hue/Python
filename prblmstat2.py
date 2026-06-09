class Vehicle:
    def __init__(self, vehicle_number):
        self.vehicle_number = vehicle_number

class ParkingManager:
    def __init__(self, hours_parked, rate_per_hour):
        self.hours_parked = hours_parked
        self.rate_per_hour = rate_per_hour

    def calculate_fee(self):
        return self.hours_parked * self.rate_per_hour

    def generate_receipt(self, vehicle):
        print("=" * 50)
        print("              PARKING RECEIPT")
        print("=" * 50)
        print(f"\nVehicle Number : {vehicle.vehicle_number}")
        print(f"Hours Parked   : {self.hours_parked}")
        print(f"\nParking Fee    : ₹{self.calculate_fee()}")
        print("\n" + "=" * 50)

vehicle = Vehicle("AP39AB1234")
parking = ParkingManager(5, 30)
parking.generate_receipt(vehicle)