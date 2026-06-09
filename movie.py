class Customer:
    def __init__(self, customer_name):
        self.customer_name = customer_name
class Movie:
    def __init__(self, movie_name, ticket_price):
        self.movie_name = movie_name
        self.ticket_price = ticket_price
class Booking:
    def __init__(self, customer, movie, number_of_tickets):
        self.customer = customer
        self.movie = movie
        self.number_of_tickets = number_of_tickets
    def book_ticket(self):
        return "CONFIRMED"
    def calculate_amount(self):
        return self.movie.ticket_price * self.number_of_tickets
    def generate_receipt(self):
        amount = self.calculate_amount()
        print("=" * 50)
        print("            MOVIE BOOKING RECEIPT")
        print("=" * 50)
        print()
        print("Customer Name   :", self.customer.customer_name)
        print("Movie Name      :", self.movie.movie_name)
        print()
        print(f"Ticket Price    : rs{self.movie.ticket_price}")
        print("Tickets Booked  :", self.number_of_tickets)
        print()
        print("-" * 50)
        print()
        print(f"Total Amount    : rs{amount}")
        print()
        print("Booking Status  :", self.book_ticket())
        print()
        print("=" * 50)
customer = Customer("Noah")
movie = Movie("Avengers", 200)
booking = Booking(customer, movie, 4)
booking.generate_receipt()