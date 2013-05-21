class PlayFinder(object):
	def __init__(self, plays=[]):
		self._plays = plays

	def _find(self, tiles):
		tiles = self.sort_tiles(tiles)
		found_plays = []
		for p in self._plays:
			for i in range(0, len(tiles)-(p.tile_count()-1)):
				tgroup = tiles[i:i+(p.tile_count())]
				if p.match(tgroup):
					found_plays.append(type(p)(tgroup))
					#print("Match:", str(tgroup[0]), str(tgroup[1]), str(tgroup[2]))
				else:
					True
					#print("No:", str(tgroup[0]), str(tgroup[1]), str(tgroup[2]))

		return found_plays

	def sort_tiles(self, tiles):
		d = [(tile.get_type(), tile.get_value(), i, tile) for i, tile in enumerate(tiles)]	
		d.sort()
		return [tile for t, v, i, tile in d]
