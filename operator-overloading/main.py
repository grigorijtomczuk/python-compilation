class Player:

	def __init__(self, name, level):
		self.name = name
		self.level = level

	def __gt__(self, other):
		return True if self.level > other.level else False

	def __eq__(self, other):
		return True if self.level == other.level else False


player1 = Player("Josh", 10)
player2 = Player("Mary", 4)

print(player1 > player2)
