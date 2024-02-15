class Book:
	_bkNum = 1

	def __init__(self, passenger, flight):
		self._passenger = passenger
		self._flight = flight
		self._bookingId = Book._bkNum
		Book._bkNum += 1

	@property
	def passenger(self):
		return self._passenger

	@property
	def flight(self):
		return self._flight

	@flight.setter
	def flight(self, flight):
		self._flight = flight

	def __str__(self):
		return f"Booking Id: {self._bookingId}\n{self.passenger}\n{self.flight}"

if __name__ == "__main__":
	from passenger import Passenger
	from flight import Flight
	from datetime import datetime
	# i. Create an empty list to store booking objects.
	bookings = []
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
	bookings.append(b1)
	bookings.append(b2)
	# v. Display the details of the bookings from the list.
	for booking in bookings:
		print(booking)
	# vi. Make changes such that both passengers are taking the same f1 flight.
	# vii. Display the details of the booking.
	# viii. Change the flight departure date for the flight that both passengers are taking.
