class Passenger:
    def __init__(self, passenger_name):
        self.passenger_name = passenger_name

class Flight:
    def __init__(self, flight_number):
        self.flight_number = flight_number

class BoardingPass:
    def __init__(self, seat_number):
        self.seat_number = seat_number

    def generate_boarding_pass(self, passenger, flight):
        print("=" * 50)
        print("               BOARDING PASS")
        print("=" * 50)
        print(f"\nPassenger Name : {passenger.passenger_name}")
        print(f"Flight Number  : {flight.flight_number}")
        print(f"Seat Number    : {self.seat_number}")
        print("\nStatus         : CHECK-IN COMPLETE")
        print("\n" + "=" * 50)

passenger = Passenger("Mason")
flight = Flight("AI202")
boarding_pass = BoardingPass("12A")
boarding_pass.generate_boarding_pass(passenger, flight)