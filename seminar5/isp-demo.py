from abc import ABC, abstractmethod

class Printer(ABC):
    @abstractmethod
    def print_document(self):
        pass

class Stapler(ABC):
    @abstractmethod
    def staple_document(self):
        pass
class Scanner(ABC):
    @abstractmethod
    def scan_document(self):
        pass


class MultiFunctionPrinter(Printer, Scanner, Stapler):
    def print_document(self):
        print("Printing")

    def staple_document(self):
        print("Stapling")

    def scan_document(self):
        print("Scanning")

class OldFashionedPrinter(Printer):
    def print_document(self):
        print("Printing")



class Photocopier(Printer, Scanner):
    def print_document(self):
        print(f"Photocopying")

    def scan_document(self):
        print(f"Scanning")



if __name__ == "__main__":
    copier = Photocopier()
    cool_printer = MultiFunctionPrinter()
    old_printer = OldFashionedPrinter()
    machines = [copier, cool_printer, old_printer]
    for machine in machines:
        machine.print_document()
        try:
            machine.staple_document()
        except:
            pass
        try:
            machine.scan_document()
        except:
            pass
        print('=====================')