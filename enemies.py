class Enemy:
	def __init__(self):
		raise NotImplementedError("Do not create raw Enemy objects.")

	def __str__(self):
		return self.name

	def is_alive(self):
		return self.hp > 0


class Goblin(Enemy):
	def __init__(self):
		self.name = "Goblin"
		self.hp = 10
		self.damage = 2


class UndeadKnight(Enemy):
	def __init__(self):
		self.name = "Undead Knight"
		self.hp = 30
		self.damage = 10


class Slime(Enemy):
	def __init__(self):
		self.name = "Slime"
		self.hp = 100
		self.damage = 1


class BossDragon(Enemy):
	def __init__(self):
		self.name = "Elemental Dragon"
		self.hp = 250
		self.damage = 20