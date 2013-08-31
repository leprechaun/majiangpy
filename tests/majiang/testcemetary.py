import random
import majiang.cemetary
import unittest
import pprint


class TestCemetary(unittest.TestCase):
	def test_cemetary_starts_with_no_tiles(self):
		c = majiang.cemetary.Cemetary()
		self.assertEqual(len(c.get_tiles_all()), 0)

	def test_cemetary_accepts_discards(self):
		c = majiang.cemetary.Cemetary()
		c.discard(majiang.tiles.Dragon(1))

	def test_cemetary_returns_all_tiles(self):
		c = majiang.cemetary.Cemetary()
		dragon = majiang.tiles.Dragon(1)
		c.discard(dragon)
		t = c.get_tiles_all()
		self.assertEqual(t[0], dragon)

	def test_cemetary_filters_on_type(self):
		c = majiang.cemetary.Cemetary()
		for v in range(1, 5):
			c.discard(majiang.tiles.Bamboo(v))
			c.discard(majiang.tiles.Number(v))
			c.discard(majiang.tiles.Circle(v))

		bamboos = c.get_tiles_of_type("bamboo")
		for t in bamboos:
			self.assertIsInstance(t, majiang.tiles.Bamboo)

	def test_cemetary_filters_on_type_and_value(self):
		c = majiang.cemetary.Cemetary()
		for v in range(1, 5):
			c.discard(majiang.tiles.Bamboo(v))
			c.discard(majiang.tiles.Number(v))
			c.discard(majiang.tiles.Circle(v))

		b4 = c.get_tiles_of_type_and_value("bamboo", 4)
		self.assertTrue(len(b4), 1)
		b4 = b4[0]
		self.assertIsInstance(b4, majiang.tiles.Bamboo)
		self.assertEqual(b4.get_value(), 4)

if __name__ == "__main__":
	unittest.main()
