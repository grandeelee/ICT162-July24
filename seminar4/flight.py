from datetime import datetime
class Flight:
    def __init__(self, flightNo, destination, departureDate, fare):
        self._flightNo = flightNo
        self._destination =destination
        self._departureDate = departureDate
        self._fare = fare
        
    @property
    def flightNo(self):
        return self._flightNo
    
    @property
    def destination(self):
        return self._destination
    
    @property
    def departureDate(self):
        return self._departureDate
    
    @property
    def fare(self):
        return self._fare

    @flightNo.setter
    def flightNo(self, flightNo):
        self._flightNo = flightNo
    
    @departureDate.setter
    def departureDate (self, departureDate):
        self._departureDate = departureDate
    def __str__(self):
        return 'Flight: {} Destination: {}  Departure Date: {:%d/%m/%Y %H:%M } Fare: {}'.format(
            self._flightNo, self._destination, self._departureDate, self.fare
        )
    

if __name__ == "__main__":
    f1 = Flight("SQ308", "London", datetime.now(), 500)
    print(f1)