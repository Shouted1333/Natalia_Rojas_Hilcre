class Ticket:
    def get_price(self):
        pass

class FlightTicket(Ticket):
    def get_price(self):
        return 200
    
def print_ticket_price(ticket):
    print(f'The price of the ticket is {ticket.get_price()}')
flight_ticket = FlightTicket() 
print_ticket_price(flight_ticket)
