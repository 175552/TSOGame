import items
import random
class Enemy:
	name = "Do not create raw enemies!"
	description = "There is no description here because you should not create raw Enemy objects!"
	attack_description = "There is no attack_description here because you should not create raw Enemy objects!"
	effects = []
	hp = 0
	damage = 0
	exp = 0
	loot = []
	poisonDamage = 0
	agro = False	# Used to cause enemies to attack spontaneously.
	
	def __init__(self, direction = None, loot = []):
		if(direction == 'n'):
			self.direction = 'north'
		elif(direction == 's'):
			self.direction = 'south'
		elif(direction == 'e'):
			self.direction = 'east'
		elif(direction == 'w'):
			self.direction = 'west'
		else:
			self.direction = None
		
		if(len(self.loot) > 0):
			for item in loot:
				self.loot.append(item)
		else:
			self.loot = loot

	def __str__(self):
		return self.name
		
	def check_text(self):
		text = ""
		if(self.direction):
			text = "The %s is blocking your progress to the %s." % (self.name, self.direction)
		text += " " + self.description			
		return text

	def take_damage(self, amount):
		damage_text = ""
		if(not self.effects == None):
			for effect in self.effects:
				if(effect == 'poison'):
					self.poisonDamage += 2
					self.hp -= self.poisonDamage
					damage_text += "The " + self.name + " is poisoned and took " + str(self.poisonDamage) + " poison damage."
				if(effect == 'burn'):
					self.hp -= 5
					damage_text += "The " + self.name + " is burned so it take 5 damage. The " + self.name + " has " + str(self.hp) + " health left."
		self.hp -= amount
		if(self.hp <= 0):
			self.hp = 0
			self.poisonDamage = 0
			defeat_text = "The %s is defeated." % self.name
			if(len(self.loot) > 0):
				defeat_text += " It dropped the following items: "
				for item in self.loot:
					defeat_text += " *" + str(item) 
			defeat_text += " You gained " + str(self.exp) + " exp"
			return defeat_text
		else:
			return damage_text + "The %s took %d damage from you. It has %s health left." % (self.name, amount, str(self.hp))
			
	def is_alive(self):
		return self.hp > 0
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]


class FallenSoldier(Enemy):
	name = "Fallen Soldier"
	description = "The fallen soldier draws its sword and silently screams, its ghost-like body transparent by torch light."
	hp = 10
	damage = 2
	goldCoins = items.Gold_Coins("Gold Coins glisten on the ground")
	goldCoins.Gold_Amount(random.randint(3, 5))
	loot = [goldCoins]
	exp = 5

class FallenBarbarian(Enemy):
	name = "Fallen Barbarian"
	description = "The fallen barbarain hefts its axe and charges."
	hp = 15
	exp = 15
	damage = 15
	goldCoins = items.Gold_Coins("Gold Coins glisten on the ground")
	goldCoins.Gold_Amount(random.randint(5, 10))
	loot = [goldCoins, items.Red_Potion()]
	agro = True
class DarkKnight(Enemy):
	name = "Dark Knight"
	description = "The dark knight's body is wrapped in darkness, absorbing all light."
	hp = 100
	damage = 4
	exp = 40
	goldCoins = items.Gold_Coins("Gold Coins glisten on the ground")
	goldCoins.Gold_Amount(random.randint(10, 20))
	loot = [goldCoins, items.Red_Potion("You see a red potion rolling on the ground")]
	agro = True


class DarkWizard(Enemy):
	name = "Dark Wizard"
	description = "A dark wizard suddenly appears from the shadows, a shiny special key glistening on his belt."
	hp = 50
	damage = 15
	exp = 50
	goldCoins = items.Gold_Coins("Gold Coins glisten on the ground")
	goldCoins.Gold_Amount(random.randint(20, 30))
	loot = [goldCoins, items.Special_Key("A special key sits on the ground, perfect for opening locked chests.")]

class BossOgre(Enemy):
	name = "Ogre"
	description = "The ogre roars and the stench of rotting flesh fills the air. Standing to it's full height, the ogre is around 13 feet tall."
	hp = 100
	damage = 20
	exp = 75
	loot = [items.Mountain_of_Gold("A mountain of gold lies in the remains of the huge ogre."), items.Red_Potion("A mysterious red potion rests peacefully on the ground."), items.Special_Key("A special key sits on the ground, perfect for.")]

class BossSlime(Enemy):
	name = "Unholy Slime"
	description = "The slime fixes its beady eyes on your body, giving you a chill through your spine."
	hp = 150
	damage = 25
	exp = 100
	loot = [items.Mountain_of_Gold("A mountain of gold lies in the remains of the huge slime."), items.Slime_Ring("A weird slime ring lies on the ground")]

class BossElf(Enemy):
	name = "Elf"
	description = "The elf unsheaths her sword, yelling a defiant battle cry"
	hp = 100
	damage = 35
	exp = 150
	loot = [items.Ring_Of_Remembrance("The ring of remembrance lies on the ground")]