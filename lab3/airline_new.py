class Airline:
	def __init__ (self, name):
		self._name = name
		self._bookings = {}

	def addBooking(self, booking):
		if not booking._bookingId in self._bookings:
			self._bookings[booking._bookingId] = booking
			return True
		return False
	
	def search(self, bookingId):
		if bookingId in self._bookings:
			return self._bookings[bookingId]

	def deleteBooking(self, bookingId):
		if bookingId in self._bookings:
			del self._bookings[bookingId]
			return True
		return False

	def changeBooking(self, bookingId, flight):
		if bookingId in self._bookings:
			self._bookings[bookingId].flight = flight
			return True
		return False

	def __str__(self):
		return "\n\n".join([str(i) for i in self._bookings.values()])

if __name__ == "__main__":
	from passenger import Passenger
	from flight import Flight
	from newbook import Book
	from datetime import datetime
	# i. Create an empty list to store booking objects.
	a1 = Airline("test")
	# ii. Create 2 Passenger objects p1 and p2.
	p1 = Passenger("pp123", "James")
	p2 = Passenger("pp234", "John")
	# iii. Create 2 Flight objects f1 and f2.
	f1 = Flight("SQ1", "NY", datetime(2024, 12, 23, 10, 59))
	f2 = Flight("SQ2", "DPS", datetime(2024, 9, 23, 10, 59))
	# iv. Create 2 booking objects for the passengers and flights created and add to the list,
	b1 = Book(p1, f1)
	b2 = Book(p2, f2)
	# p1 taking f1 and p2 taking f2.
	a1.addBooking(b1)
	a1.addBooking(b2)
	# v. Display the details of the bookings from the list.
	print(a1)
	

	