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
        self.assertEqual(types.count(majiang.plays.Sequence), 1)

    def test_dragons_dont_sequence(self):
        tiles = [
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(2),
            majiang.tiles.Dragon(3),
        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        self.assertEqual(len(finds), 0)

    def test_winds_dont_sequence(self):
        tiles = [
            majiang.tiles.Wind(1),
            majiang.tiles.Wind(2),
            majiang.tiles.Wind(3),
        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        self.assertEqual(len(finds), 0)

    def test_find_one_sequence(self):
        tiles = [
            majiang.tiles.Bamboo(1),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
            majiang.tiles.Bamboo(4),
            majiang.tiles.Bamboo(5),
        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        self.assertEqual(len(finds), 1)

    def test_find_two_sequences(self):
        tiles = [
            majiang.tiles.Bamboo(1),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
            majiang.tiles.Bamboo(4),
            # 5 is missing here
            majiang.tiles.Bamboo(6),
            majiang.tiles.Bamboo(7),
            majiang.tiles.Bamboo(8),
            majiang.tiles.Bamboo(9),

        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        self.assertEqual(len(finds), 2)
        self.assertEqual(type(finds[0]), majiang.plays.Sequence)
        self.assertEqual(type(finds[1]), majiang.plays.Sequence)

    def test_find_two_overlapping_sequences(self):
        tiles = [
            majiang.tiles.Bamboo(1),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
            majiang.tiles.Bamboo(4),

            majiang.tiles.Bamboo(1),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
            majiang.tiles.Bamboo(4),

        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles, find_sames=False)

        self.assertEqual(len(finds), 2)
        self.assertEqual(type(finds[0]), majiang.plays.Sequence)
        self.assertEqual(type(finds[1]), majiang.plays.Sequence)

    def test_find_two_partially_overlapping_sequences_1(self):
        tiles = [
            majiang.tiles.Bamboo(1),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
            majiang.tiles.Bamboo(4),

            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),

        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles, find_sames=False)

        seq = majiang.plays.Sequence()

        self.assertEqual(len(finds), 2)

        self.assertEqual(type(finds[0]), majiang.plays.Sequence)
        self.assertEqual(finds[0].tile_count(), 4)
        self.assertEqual(finds[0].min(), 1)
        self.assertEqual(finds[0].max(), 4)
        self.assertEqual(seq.match(finds[0]._tiles), True)

        self.assertEqual(type(finds[1]), majiang.plays.Sequence)
        self.assertEqual(finds[1].tile_count(), 2)
        self.assertEqual(finds[1].min(), 2)
        self.assertEqual(finds[1].max(), 3)
        self.assertEqual(seq.match(finds[1]._tiles), True)

    def test_find_two_partially_overlapping_sequences_and_two_eyes(self):
        tiles = [
            majiang.tiles.Bamboo(1),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
            majiang.tiles.Bamboo(4),

            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),

        ]

        random.shuffle(tiles)

        finder = majiang.playfinder.PlayFinder()
        finds = finder.find(tiles)

        seq = majiang.plays.Sequence()

        self.assertEqual(len(finds), 4)

        self.assertEqual(type(finds[0]), majiang.plays.Eyes)
        self.assertEqual(type(finds[1]), majiang.plays.Eyes)

        self.assertEqual(type(finds[2]), majiang.plays.Sequence)
        self.assertEqual(finds[2].tile_count(), 4)
        self.assertEqual(finds[2].min(), 1)
        self.assertEqual(finds[2].max(), 4)
        self.assertEqual(seq.match(finds[3]._tiles), True)

        self.assertEqual(type(finds[3]), majiang.plays.Sequence)
        self.assertEqual(finds[3].tile_count(), 2)
        self.assertEqual(finds[3].min(), 2)
        self.assertEqual(finds[3].max(), 3)
        self.assertEqual(seq.match(finds[3]._tiles), True)
