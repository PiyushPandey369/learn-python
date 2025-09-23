'''
    Plane Ticket Booking System

    Write a Class 'Plane’ which has methods to book a ticket, get status (no of seats) 
    and get fare information of train running under Nepal Airlines.

'''
from random import randint

class Plane:
    
    def __init__(self):
        self.ticketNo=randint(0,100)
    
    def book_ticket(self,from1,destination):
        print(f"Ticket booked for Flight no: {self.ticketNo} {from1} to {destination}")
    
    def get_status(self,from1,destination):
       print(f"Flight no: {self.ticketNo} flight is flying a new high {from1} to {destination}")
    
    def get_fare(self,from1,destination):
        print(f"Flight no: {self.ticketNo} from {from1} to {destination} will cost {randint(1000,8000)}")

p=Plane()
p.book_ticket("Kathmandu","Dhangadi")
p.get_fare("Kathmandu","Dhangadi")
p.get_status("Kathmandu","Dhangadi")