import majiang
import majiang.wall
import unittest
import pprint


class TestWall(unittest.TestCase):
	def test_wall_starts_with_136_tiles(self):
		w = majiang.wall.Wall()
		self.assertEqual(136, w.tiles_left())

	def test_wall_has_the_correct_number_of_each_tile(self):
		w = majiang.wall.Wall()
		tiles = {}

		# Run through the keys
		for i in range(1, 137):
			t = w.draw_tile()

			# Divide the tiles into buckets by type
			if t.get_type() not in tiles:
				tiles[t.get_type()] = {}

			# Divive the typed keys into buckets by value
			if t.get_value() not in tiles[t.get_type()]:
				tiles[t.get_type()][t.get_value()] = []

			# Actually append the tile into the proper hierarchal bucket
			tiles[t.get_type()][t.get_value()].append(t)

		# By asserting there are 5 keys, there are 5 distinct types
		self.assertEqual(len(tiles), 5)

		# Then checking 5 keys explicitely, no invalid types can exist
		self.series_is_complete(tiles["dragon"], [1, 2, 3])
		self.series_is_complete(tiles["wind"], [1, 2, 3, 4])
		self.series_is_complete(tiles["number"], [1, 2, 3, 4, 5, 6, 7, 8, 9])
		self.series_is_complete(tiles["circle"], [1, 2, 3, 4, 5, 6, 7, 8, 9])
		self.series_is_complete(tiles["bamboo"], [1, 2, 3, 4, 5, 6, 7, 8, 9])

	def test_wall_can_draw_any_number_of_available_tiles(self):
		w = majiang.wall.Wall()
		self.assertEqual(len(w.draw_tile(3)), 3)
		self.assertEqual(len(w.draw_tile(5)), 5)
		self.assertEqual(len(w.draw_tile(14)), 14)

	def series_is_complete(self, series, range):
		for v in range:
			self.assertEqual(len(series[v]), 4)

if __name__ == "__main__":
	unittest.main()
