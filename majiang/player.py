class Player:
	def __init__(self,name):
		self._name = name
		self._tiles = []

	def draw_initial_tiles(self,tiles):
		for t in tiles:
			self._tiles.append( t )

	def take_draw(self,tile):
		pass

	def take_discard(self):
		return tile

	def offer_discard(self,tile):
		# must return a Play
		return None

	def get_name(self):
		return self._name
