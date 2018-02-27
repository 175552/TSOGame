import random

class MapTile:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y
	
	def intro_text(self):
		raise NotImplementedError("Create a subclass instead!")


class StartTile(MapTile):
	def intro_text(self):
		return "(you hear a distant voice) " \
	"Hello...and welcome to DungeonEscape..." \
	"You are trapped in a dungeon...escape and your memories" \
	" will be returned. Type in commands to move around the map." \
	"This tile is a safe tile. When you enter a room you must first" \
	"Clear the room of all monsters. Some rooms may have chests, so look carerfully!"


class MonsterTile(MapTile):
	def intro_text(self):
		goblinNumber = random.randint(1, 3)
		description = "You enter an easy room. You look around and see " + str(goblinNumber) + " goblins"
		return description
		
class WeaponTile
(MapTile):
	def intro_text(self):
		return """You've entered a secret room. Don't tell anyone!"""
		
class DeathTile(MapTile):
	def intro_text(self):
		return """You've died. Try harder, stupid!"""


class VictoryTile(MapTile):
	def intro_text(self):
		return """You see a bright light in the distance...
		It grows as you get closer! It's sunlight!	
		Victory is yours!
		"""
		
class World:									# I choose to define the world as a class. This makes it more straightforward to import into the game.
	map = [
		[None, 			VictoryTile(), 			None, 				None, 				None],
		[None, 			MonsterTile(), 			None, 				DeathTile(), 			None],
		[MonsterTile(), 		StartTile(), 			MonsterTile(), 			SecretTile(), 			None],
		[None, 			MonsterTile(), 			None, 				None, 				None],
		[None,			DeathTile(),			None,				None,				None]
	]
	
	def __init__(self):
		for i in range(len(self.map)):			# We want to set the x, y coordinates for each tile so that it "knows" where it is in the map.
			for j in range(len(self.map[i])):	# I prefer to handle this automatically so there is no chance that the map index does not match
				if(self.map[i][j]):				# the tile's internal coordinates.
					self.map[i][j].x = j
					self.map[i][j].y = i
					
	def tile_at(self, x, y):
		if x < 0 or y < 0:
			return None
		try:
			return self.map[y][x]
		except IndexError:
			return None
			
	def check_north(self, x, y):
		if y-1 < 0:
			room = None
		try:
			room = self.map[y-1][x]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the north."]
		else:
			return [False, "There doesn't seem to be anything to the north."]
			
	def check_south(self, x, y):
		if y+1 < 0:
			room = None
		try:
			room = self.map[y+1][x]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the south."]
		else:
			return [False, "There doesn't seem to be anything to the south."]

	def check_west(self, x, y):
		if x-1 < 0:
			room = None
		try:
			room = self.map[y][x-1]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the west."]
		else:
			return [False, "There doesn't seem to be anything to the west."]
			
	def check_east(self, x, y):
		if x+1 < 0:
			room = None
		try:
			room = self.map[y][x+1]
		except IndexError:
			room = None
		
		if(room):
			return [True, "You head to the east."]
		else:
			return [False, "There doesn't seem to be anything to the east."]
