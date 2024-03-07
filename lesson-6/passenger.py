class Passenger: 
    def __init__(self, ppNo:str , name:str, yearBorn:int):
        self._ppNo = ppNo
        self._name = name
        self._yearBorn = yearBorn
        
    @property 
    def ppNo(self): 
        return self._ppNo
    
    @property
    def name(self): 
        return self._name
    
    @property
    def yearBorn(self): 
        return self._yearBorn
    
    def __str__(self): 
        return f'Passport No: {self.ppNo}\tName: {self.name}\tBorn in: {self.yearBorn}'
    

if __name__ == "__main__":
    p1 = Passenger("E1234", "John", 2000)
    print(p1)
