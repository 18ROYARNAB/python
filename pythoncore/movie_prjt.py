class movie_prj:
    def __init__(self,movie_name : str,ticket_price : int):
        self.movie_name=movie_name
        self.total_seats=500
        self.ticket_price=ticket_price
        self.booked_seats=0
        
    def book_ticket(self,num_tickets):
        if num_tickets > self.total_seats - self.booked_seats:
            print("not enoughs seats")
        else:
            self.booked_seats += num_tickets
            self.total_seats -= num_tickets
            print("Your ticket is booked ")
            print(f"Ticket price : {self.ticket_price * num_tickets}")
    def show_status(self):
        print(f"seats available : {self.total_seats}")
        print(f"Movie name : {self.movie_name}, Seats available : {self.total_seats}")
        print(f"TOtal booked setas : {self.booked_seats}")

movie=movie_prj("krish",502)
movie.book_ticket(50)
movie.book_ticket(60)

movie.show_status()