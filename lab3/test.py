class Card:
    def __init__(self, number, balance):
        self._number = number
        self._balance = balance
		
    def __eq__(self, other):
        return self._number == other._number

class Bank:
	def __init__(self):
		self._cards = []

	def addCard(self, card):
		if card not in self._cards:
			self._cards.append(card)
		else:
			raise Exception("card exist")

if __name__ == "__main__":
    b1 = Bank()
    c1 = Card("123", 100)
    c2 = Card("123", 100)
    c3 = Card("123", 100)
    b1.addCard(c1)
    b1.addCard(c2)
    b1.addCard(c3)
    print(c1 == c2)
    print(b1._cards[0] == b1._cards[1])