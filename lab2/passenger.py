class Passenger:
    def __init__(self, ppNo, name):
        self._ppNo = ppNo
        self._name = name

    @property
    def ppNo(self):
        return self._ppNo

    @property
    def name(self):
        return self._name
    
    def __str__(self):
        return f"Passport No: {self.ppNo}\tName: {self.name}"
