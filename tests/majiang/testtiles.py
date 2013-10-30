import majiang.tiles
import unittest


class TestTiles(unittest.TestCase):
    def test_tiles_has_proper_to_string(self):
        t = majiang.tiles.Bamboo(1)
        self.assertEqual(str(t),"bamboo-1")

    def test_tiles_construct_raises_when_out_of_bounds(self):
        self.assertRaises(Exception, majiang.tiles.Tile, ("bamboo", 0))

class TestWind(unittest.TestCase):
    def test_wind_construct_raises_when_out_of_bounds(self):
        self.assertRaises(Exception, majiang.tiles.Wind, (0))
        self.assertRaises(Exception, majiang.tiles.Wind, (5))


if __name__ == "__main__":
    unittest.main()
