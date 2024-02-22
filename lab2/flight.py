from datetime import datetime


class Flight:
    def __init__(self, flightNo, destination, departureDate):
        self._flightNo = flightNo
        self._destination = destination
        self._departureDate = departureDate

    @property
    def flightNo(self):
        return self._flightNo

    @property
    def destination(self):
        return self._destination

    @property
    def departureDate(self):
        return self._departureDate

    @flightNo.setter
    def flightNo(self, flightNo):
        self._flightNo = flightNo

    @departureDate.setter
    def departureDate(self, departureDate):
        self._departureDate = departureDate

    def __str__(self):
        return f'Flight: {self._flightNo} Destination: {self._destination} Departure Date: {self._departureDate:%d/%m/%Y %H:%M }'
