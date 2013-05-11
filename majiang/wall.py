from random import shuffle
import majiang
from majiang.wall import *
from majiang.tiles import *

class Wall:
	def __init__(self):
		self._tiles = []

		# THERE ARE FOUR OF EACH TILE
		for i in range( 0, 4 ):
			# WINDS - HAVE 4 VALUES
			for v in range( 1, 5 ):
				self._tiles.append( majiang.tiles.Wind( v ) )

			# DRAGONS - HAVE 3 VALUES
			for v in range( 1, 4 ):
				self._tiles.append( majiang.tiles.Dragon( v ) )

			# BAMBOOS, NUMBERS AND CIRCLES - HAVE 9 VALUES
			for v in range( 1, 10 ):
				# BAMBOO
				self._tiles.append( majiang.tiles.Bamboo( v ) )

				# NUMBERS
				self._tiles.append( majiang.tiles.Number( v ) )

				# DOTS
				self._tiles.append( majiang.tiles.Circle( v ) )

		# SHUFFLE THE TILES
		shuffle( self._tiles )


	def draw_tile(self):
		if len( self._tiles ) > 0:
			return self._tiles.pop()

	def tiles_left(self):
		return len( self._tiles )
