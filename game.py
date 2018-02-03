class Weapon: 
	def __str__(self):
		return self.name
class Fist(Weapon):
	def __init__(self):
		self.name = "Fist"
		self.description = "You can always trust your fists"
		self.damage = 5
class Sword(Weapon):
	def __init__(self):
		self.name = "Sword"
		self.description = "A shiny sword honed to a point"
		self.damage = 10

name = input("Enter you name: ")
print("Welcome " + name + "!")
playerWeapon = Fist()
print("(you hear a distant voice) " \
	"Hello...and welcome to DungeonEscape..." \
	"You are trapped in a dungeon...escape and your memories" \
	" will be returned. You have been equipped " \
	" with your" + playerWeapon.name)
