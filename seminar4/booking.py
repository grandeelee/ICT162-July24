from datetime import datetime
from flight import Flight
from passenger import Passenger
from abc import ABC, abstractmethod

class Booking(ABC):
    _bkNum = 1

    def __init__(self, passenger:Passenger, flight:Flight):
        
        self._bookingid = type(self)._bkNum
        type(self)._bkNum += 1
        self._passenger = passenger
        self._flight = flight
        self._bookingDate = datetime.now()
            
    @property
    def bookingid(self):
        return self._bookingid

    @property
    def passenger(self):
        return self._passenger
    
    @property
    def flight(self):
        return self._flight
            
    @flight.setter
    def flight(self, newValue):
        self._flight = newValue

    @property
    def bookingDate(self):
        return self._bookingDate

    @abstractmethod
    def ticketPrice(self):
        pass

    def __str__(self) -> str:
        return "Booking id: {}\tBooking Date: {}\n{}\n{}".format(self.bookingid, self.bookingDate, self.passenger, self.flight)

class IndividualBooking(Booking):
    _DISCOUNT = 0.2

    def __init__(self, passenger, flight):
        super().__init__(passenger, flight)

    def ticketPrice(self):
        if self.passenger.yearBorn > 2005 or self.passenger.yearBorn <= 1963:
            price = self.flight.fare * (1-type(self)._DISCOUNT)
        else:
            price = self.flight.fare
        return price

class CorporateBooking(Booking):
    _DISCOUNT = 0.5

    def __init__(self, passenger, flight, company):
        super().__init__(passenger, flight)
        self._company = company

    def ticketPrice(self):
        return self.flight.fare * (1-type(self)._DISCOUNT)
    
    def __str__(self) -> str:
        return f"Company: {self._company}\n" + super().__str__()

if __name__ == "__main__":
    bookings = []
    p1 = Passenger("E3133", "John", 2006)
    p2 = Passenger("E3132", "James", 1988)
    f1 = Flight("SQ123", "LA", datetime(2021, 12, 25, 4, 15), 500)
    f2 = Flight("SQ121", "DPS", datetime(2021, 12, 25, 4, 15), 200)
    bookings.append(IndividualBooking(p1, f1))
    bookings.append(IndividualBooking(p1, f1))
    bookings.append(CorporateBooking(p2, f2, "ABC Pte Ltd"))
    print("\n\n".join(["{}".format(i) for i in bookings]))
    print(bookings[2].ticketPrice())


