import pprint
class Cemetary(object):
	def __init__(self):
		self._tiles = []

	def discard(self,tile):
		self._tiles.append( tile )

	def get_tile_count(self):
		return len( self._tiles )

	def get_tiles_all(self):
		return self._tiles

	def get_tiles_of_type(self, type):
		returns = []
		for t in self._tiles:
			if t.get_type() == type:
				returns.append( t )
		return returns

	def get_tiles_of_type_and_value(self, type, value):
		returns = []
		r1 = self.get_tiles_of_type(type)
		for t in r1:
			if t.get_value() == value:
				returns.append( t )
		return returns
