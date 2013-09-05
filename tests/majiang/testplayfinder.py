import majiang.playfinder
import majiang.tiles
import unittest
import random


class TestPlayFinder(unittest.TestCase):
    def test_find_one_eyes_alone(self):
        tiles = [
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(1),
        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        self.assertEqual(len(finds), 1)
        self.assertIsInstance(finds[0], majiang.plays.Eyes)

    def test_find_one_peng_alone(self):
        tiles = [
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(1),
        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        self.assertEqual(len(finds), 1)
        self.assertIsInstance(finds[0], majiang.plays.Peng)

    def test_find_one_kong_alone(self):
        tiles = [
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(1),
        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        self.assertEqual(len(finds), 1)
        self.assertIsInstance(finds[0], majiang.plays.Kong)


    def test_find_one_chao_alone(self):
        tiles = [
            majiang.tiles.Circle(1),
            majiang.tiles.Circle(2),
            majiang.tiles.Circle(3),
        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        self.assertEqual(len(finds), 1)
        self.assertIsInstance(finds[0], majiang.plays.Chao)

    def test_find_many(self):
        tiles = [
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(1),

            majiang.tiles.Circle(2),
            majiang.tiles.Circle(2),
            majiang.tiles.Circle(2),

            majiang.tiles.Number(3),
            majiang.tiles.Number(3),
            majiang.tiles.Number(3),
            majiang.tiles.Number(3),

            majiang.tiles.Bamboo(1),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),

            majiang.tiles.Wind(1),
            majiang.tiles.Wind(2),
            majiang.tiles.Wind(3),
            majiang.tiles.Wind(4),
        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)


        types = [type(find) for find in finds]    

        self.assertEqual(len(finds), 4)
        self.assertEqual(types.count(majiang.plays.Eyes), 1)
        self.assertEqual(types.count(majiang.plays.Peng), 1)
        self.assertEqual(types.count(majiang.plays.Kong), 1)
        self.assertEqual(types.count(majiang.plays.Chao), 1)

    def test_find_two_identical_chaos(self):
        tiles = [
            majiang.tiles.Bamboo(1),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
            majiang.tiles.Bamboo(1),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        types = [type(find) for find in finds]    

        self.assertEqual(len(finds), 5)
        self.assertEqual(types.count(majiang.plays.Chao), 2)
        self.assertEqual(types.count(majiang.plays.Eyes), 3)

    def test_find_two_offset_chaos(self):
        tiles = [
            majiang.tiles.Bamboo(1),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
            majiang.tiles.Bamboo(3),
            majiang.tiles.Bamboo(4),
        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        types = [type(find) for find in finds]

        self.assertEqual(len(finds), 4)
        self.assertEqual(types.count(majiang.plays.Chao), 2)
        self.assertEqual(types.count(majiang.plays.Eyes), 2)

    def test_find_a_chao_and_overlapping_almost_chao(self):
        tiles = [
            majiang.tiles.Bamboo(1),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        types = [type(find) for find in finds]

        self.assertEqual(types.count(majiang.plays.Chao), 1)
        self.assertEqual(types.count(majiang.plays.Eyes), 2)
        self.assertEqual(types.count(majiang.plays.AlmostChao), 1)
        self.assertEqual(len(finds), 4)

    def test_dragons_dont_chao(self):
        tiles = [
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(2),
            majiang.tiles.Dragon(3),
        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        self.assertEqual(len(finds), 0)

    def test_winds_dont_chao(self):
        tiles = [
            majiang.tiles.Wind(1),
            majiang.tiles.Wind(2),
            majiang.tiles.Wind(3),
        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        self.assertEqual(len(finds), 0)
