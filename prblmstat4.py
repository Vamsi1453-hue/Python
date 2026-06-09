class Guest:
    def __init__(self, guest_name):
        self.guest_name = guest_name

class Room:
    def __init__(self, room_type, room_rate):
        self.room_type = room_type
        self.room_rate = room_rate

class Reservation:
    def __init__(self, nights):
        self.nights = nights

    def generate_invoice(self, guest, room):
        total = room.room_rate * self.nights

        print("=" * 50)
        print("              HOTEL INVOICE")
        print("=" * 50)
        print(f"\nGuest Name     : {guest.guest_name}")
        print(f"Room Type      : {room.room_type}")
        print(f"\nNights Stayed  : {self.nights}")
        print(f"\nTotal Amount   : ₹{total}")
        print("\n" + "=" * 50)

guest = Guest("Sophia")
room = Room("Deluxe", 3500)

reservation = Reservation(3)
reservation.generate_invoice(guest, room)