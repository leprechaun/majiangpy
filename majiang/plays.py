class Play(object):
	def __init__(self, tiles=None):
		if not tiles == None:
			self._tiles = tiles

	def get_tiles(self):
		return self._tiles

	def _get_values(self, tiles):
		values = []
		for t in tiles:
			values.append(t.get_value())
		return values

	def _get_types(self, tiles):
		types = []
		for t in tiles:
			types.append(t.get_type())
		return types

	def types_are_equal(self, tiles):
		types = self._get_types(tiles)
		return len(set(types)) == 1

	def values_are_equal(self, tiles):
		values = self._get_values(tiles)
		return len(set(values)) == 1

	def values_are_sequential(self, tiles):
		values = self._get_values(tiles)

		# all values must be unique
		if len(set(values)) < len(values):
			return False

		if max(values) == (min(values) + len(values) - 1):
			return True

		return False


class Eyes(Play):
	def tile_count(self):
		return 2

	def match(self, tiles):
		if not len(tiles) == 2:
			return False

		if not self.types_are_equal(tiles):
			return False

		if not self.values_are_equal(tiles):
			return False

		return True


class Peng(Play):
	def tile_count(self):
		return 3

	def match(self, tiles):
		if len(tiles) != 3:
			return False

		if self.types_are_equal(tiles) and self.values_are_equal(tiles):
			return True
		else:
			return False


class Chao(Play):
	def tile_count(self):
		return 3

	def match(self, tiles):
		if not len(tiles) == 3:
			return False

		if not tiles[0].can_chao():
			return False

		if not self.types_are_equal(tiles):
			return False

		if not self.values_are_sequential(tiles):
			return False

		return True

class AlmostChao(Play):
	def tile_count(self):
		return 2

class Kong(Play):
	def tile_count(self):
		return 4

	def match(self, tiles):
		if not len(tiles) == 4:
			return False

		if not self.types_are_equal(tiles):
			return False

		if not self.values_are_equal(tiles):
			return False

		return True


class Majiang(Play):
	def match(self, plays):
		tile_count = 0
		for p in plays:
			tile_count = tile_count + len(p.get_tiles())

		# expect 4 pengs/chaos and a pair
		if tile_count == 14:
			return True
		# expect 3 pengs/chaos, a kong and a pair
		elif tile_count == 15:
			return True
