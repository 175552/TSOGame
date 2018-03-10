from random import randint 	# Used to generate random integers.
import random
class Item:
	name = "Do not create raw Item objects!"
	
	description = "You should define a description for items in their subclass."
	dropped_description = "You should define the description for this item after it is dropped in its subclass."
	
	is_dropped = False	# This is going to store the status of whether this item has been picked up and dropped before.
	
	value = 0		# Used to establish value if item is for sale.
	
		
	def __init__(self, description = "", value = 0):
		if(description):
			self.intro_description = description
		else:
			self.intro_description = self.dropped_description
		
		if(self.value == 0):
			self.value = value
			
	def __str__(self):
		return self.name	

	def room_text(self):
		if(not self.is_dropped):					# We may want to have a different description for a weapon the first time it is encountered vs. after it has been dropped.
			return self.intro_description
		else:
			return self.dropped_description

	def check_text(self):
		return self.description
		
	def drop(self):
		if(self.name == 'ring of remembrance'):
			return "This item cannot be dropped"
		self.is_dropped = True
		
	def pick_up(self):
		self.is_dropped = False
		
	def handle_input(self, verb, noun1, noun2, inventory):
		return [False, None, inventory]
class Ring_Of_Remembrance(Item):
	name = "ring of remembrance"

	description = "A plain iron ring with the word Neo, printed on it"
	isDropped = False

class Slime_Ring(Item):
	name = "slime ring"

	description = "A mysterious ring that is obtained from defeating the Unholy Slime"
	dropped_description = "The slime ring is on the ground"
class Parchment(Item):
	name = "parchment"

	description = "The Parchment reads: The Final Test..."
	dropped_description = "A piece of parchment is on the ground."
class Special_Key(Item):
	name = "special key"

	description = "A special key that looks like it can open locked chests."
	dropped_description = "A special key is lying on the ground."

class Iron_Key(Item):
	name = "iron key"
	
	description = "An old iron key. It looks like it would open a massive door."
	dropped_description = "An old iron key is lying on the ground."		
		
		
class Consumable(Item):
	consume_description = "You should define flavor text for consuming this item in its subclass."

	healing_value = 0		# Define this appropriately in your subclass.
		
	def consume(self):
		return [self.consume_description, self.healing_value]
			
class Crusty_Bread(Consumable):
	name = "crusty bread"
	healing_value = 10
	
	description = "Just a stale old piece of bread."
	dropped_description = "A piece of crusty bread is lying on the ground."
	consume_description = "You eat the crusty piece of bread."
			
class Red_Potion(Consumable):
	name = "red potion"
	healing_value = 30
	
	description = "A bottle of mysterious, glowing red potion. For some reason it looks healthy. Be warned: You can only hold one potion at a time, so drink these quickly!"
	dropped_description = "A bottle of red potion is glowing on the ground."
	consume_description = "You drink the glowing red potion."
	
	
	

class Weapon(Item):	
	equip_description = "You should define flavor text for equipping this item in its subclass."
	attack_descriptions = ["You should define one or more attack descriptions as a list in your subclass.", "This is an example secondary attack description"]
	critChance = 0
	crit = False
	damage = 0		# Define this appropriately in your subclass.
	effects = []
	
	def get_damage(self):
		return self.damage

	def equip_text(self):
		return self.equip_description
			
	def attack(self):
		return [self.attack_descriptions[randint(0, len(self.attack_descriptions)-1)], self.damage]		# Return damage and a random attack description from your list.
		
	def critMaybe(self):
		chance = random.randint(1, 100)
		if(self.critChance * 100 > chance):
			self.crit = True

	def get_effects(self):
		returnText = ""
		x = 0
		for x in range(0, len(self.effects)):
			returnText += str(self.effects[x])
		return returnText

class Rock(Weapon):
	name = "rock"
	
	description = "A fist-sized rock, suitable for bludgeoning."
	dropped_description = "A fist-sized rock lies on the ground. It looks like it could be used as a weapon... or something. (5 damage)"
	equip_description = "You arm yourself with the rock."
	attack_descriptions = ["You swing the rock as hard as you can. Crack!", "You wind up and chuck the rock at your enemy. Oof."]
	critChance = .2
	crit = False
	damage = 5
	effects = None


class Dagger(Weapon):
	name = "dagger"
	
	description = "A small dagger with some rust. It looks pretty sharp. (10 damage)"
	dropped_description = "A dagger lies on the ground. It looks somewhat more dangerous than a rock."
	equip_description = "You take the dagger in your hand."
	attack_descriptions = ["You lunge forward with the dagger.", "You stab wildly with the dagger.", "You swing the dagger at your foe."]
	critChance = .3
	crit = False
	damage = 10
	effects = None

class Poison_Dagger(Weapon):
	name = "poison dagger"
	description = "A dagger with the tip glowing with a deadly green glow"
	equip_description = "You take the poison dagger in your hand."
	attack_descriptions = ["You jab with the poison dagger.", "You swing the poison dagger.", "You stab the dagger at the enemies body."]

	effects = ["poison"]

	critChance = .35
	crit = False
	damage = 11

class Flame_Sword(Weapon):
	name = "flame sword"
	
	description = "A flame sword that was forged by the ancient golems. It burns with the light of a thousand souls. (20 damage)"
	dropped_description = "There is a flame sword lying on the ground."
	equip_description = "You arm yourself with the flame sword."
	attack_descriptions = ["You slash with your flame sword.", "Your flame sword connects mightily with your enemy.", "You swing the flame sword with all your might."]
	critChance = .25
	crit = False
	damage = 20

	effects = ["burn"]

class Gold(Item):
	value = 0		# Define this appropriately in your subclass.
	name = "Don't make gold classes"
	def obtain_text(self):
		return "%i gold was added to your inventory." % value

		
class Gold_Coins(Gold):
	name = "gold coins"	
	description = "A small handful of gold coins."
	dropped_description = "A shiny handful of gold coins is lying on the ground."

	def Gold_Amount(self, amount):
		self.value = amount	

class Mountain_of_Gold(Gold):
	name = "mountain of gold"
	value = 100		
	
	description = "A lustrous mountain of gold coins."
	dropped_description = "A lustrous mountain of gold coins is lying on the ground."
	
	
class Container:
	name = "Do not create raw Container objects!"
	locked = False
	closed_description = "You should define a closed description for containers in their subclass."
	open_description = "You should define an open description for containers in their subclass."
	
	closed = True
	
	contents = []
	
	def __init__(self, items = []):
		for item in items:
			if(len(self.contents) == 0):
				self.contents = [item]
			else:
				self.contents.append(item)
	
	def add_item(self, item):
		if(len(self.contents) == 0):
			self.contents = [item]		# Initialize the list if it is empty.
		else:
			self.contents.append(item)	# Add to the list if it is not empty.
			
	def remove_item(self, item):
		removal_index = -1
		for index in range(len(self.contents)):
			if(self.contents[index].name == item.name):
				removal_index = index
		if(removal_index >= 0):
			self.contents.pop(removal_index)
	
			
	def __str__(self):
		return self.name	

	def room_text(self):
		if(self.closed):					# We may want to have a different description for a container if it is open or closed.
			return self.closed_description
		else:
			return self.open_description

	def check_text(self):
		if(self.closed):
			return self.closed_description
		else:
			if(len(self.contents) > 0):
				print("The %s contains:" % self.name)
				for item in self.contents:
					if(str(item).title() == 'Gold Coins'):
						print('* ' + str(item.value) + ' gold coins')
					else:
						print('* ' + str(item).title())
			else:
				return "The %s is empty." % self.name
		
	def handle_input(self, verb, noun1, noun2, inventory):			
		return [False, "", inventory]

class Locked_Chest(Container):
	name = "locked chest"
	closed_description = "A locked chest sits against the far wall, its lid shut tightly."
	open_description = "A locked chest sits against the far wall, its lid open wide."
	locked = True

	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == self.name):
			if(verb == 'check'):
				if(self.locked):
					return[True, "The chest is locked. You need a special key to open it.", inventory]
				else:
					return [True, self.check_text(), inventory]
			if(verb == 'open'):
				if(self.locked):
					return [True, "The chest is locked. You need a special key to open it.", inventory]
				else:
					if(self.closed == True):
						self.closed = False
						return [True, "You pry the lid of the locked chest open.", inventory]
					else:
						return [True, "The locked chest is already wide open.", inventory]
			if(verb == 'unlock'):
				if(self.locked):
					if(noun2 == 'special key'):
						for index in range(len(inventory)):
							if(inventory[index].name.lower() == 'special key'):
								inventory.pop(index)	# Removes the item at this index from the inventory.
								self.locked = False
								return [True, "You insert the iron key into the locked chest and twist. The chest unlocks with a click.", inventory]
						return [True, "You don't seem to have the right key for this chest.", inventory]
					elif(noun2 == 'key'):
						return [True, "Be more specific. This chest only takes a specific key.", inventory]
					else:
						return [True, "What item do you plan to unlock that chest with?", inventory]
				else:
					return [True, "The chest is already unlocked.", inventory]
			if(verb == 'close'):
				if(self.closed == False):
					self.closed = True
					return [True, "You push down the lid of the locked chest and it closes with a bang.", inventory]
				else:
					return [True, "The locked chest is already closed.", inventory]
		elif(noun1):
			if(verb == 'take'):
				if(not self.closed):
					for index in range(len(self.contents)):
						if(self.contents[index].name.lower() == noun1):
							if(isinstance(self.contents[index], Item)):
								pickup_text = "You took the %s from the old chest and added it to your inventory." % self.contents[index].name
								inventory.append(self.contents[index])
								self.contents.pop(index)
								return [True, pickup_text, inventory]
							else:
								return [True, "The %s is too heavy to pick up." % self.contents[index].name, inventory]
			if(verb == 'check'):
				if(not self.closed):
					for index in range(len(self.contents)):
						if(self.contents[index].name.lower() == noun1):
							if(isinstance(self.contents[index], Item)):
								return [True, self.contents[index].check_text(), inventory]
		return [False, None, inventory]
class Old_Chest(Container):
	name = "old chest"
	closed_description = "A battered old chest sits against the far wall, its lid shut tightly."
	open_description = "A battered old chest sits against the far wall, its lid open wide."
	locked = False

	def handle_input(self, verb, noun1, noun2, inventory):
		if(noun1 == self.name):
			if(verb == 'check'):
				return [True, self.check_text(), inventory]
			if(verb == 'open'):
				if(self.closed == True):
					self.closed = False
					return [True, "You pry the lid of the battered old chest open.", inventory]
				else:
					return [True, "The old chest is already wide open.", inventory]
			if(verb == 'close'):
				if(self.closed == False):
					self.closed = True
					return [True, "You push down the lid of the old chest and it closes with a bang.", inventory]
				else:
					return [True, "The old chest is already closed.", inventory]
		elif(noun1):
			if(verb == 'take'):
				if(not self.closed):
					for index in range(len(self.contents)):
						if(self.contents[index].name.lower() == noun1):
							if(isinstance(self.contents[index], Item)):
								pickup_text = "You took the %s from the old chest and added it to your inventory." % self.contents[index].name
								inventory.append(self.contents[index])
								self.contents.pop(index)
								return [True, pickup_text, inventory]
							else:
								return [True, "The %s is too heavy to pick up." % self.contents[index].name, inventory]
			if(verb == 'check'):
				if(not self.closed):
					for index in range(len(self.contents)):
						if(self.contents[index].name.lower() == noun1):
							if(isinstance(self.contents[index], Item)):
								return [True, self.contents[index].check_text(), inventory]
		return [False, None, inventory]
