class Player:
	def __init__(self,name,wind):
		self._name = name
		self._wind = wind
		self._tiles = []

	def draw_initial_tiles(self,tiles):
		for t in tiles:
			self._tiles.append( t )

	def draw_tile(self,tile):
		# must return a Tile
		return tile

	def offer_discard(self,tile)
		# must return a Play
		return None
