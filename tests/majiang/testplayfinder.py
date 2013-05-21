import majiang.accountant
import majiang.player
import majiang.tiles
import majiang.playfinder
import unittest
import pprint
import random


class TestPlayFinder(unittest.TestCase):
	def test_find_one_eyes_alone(self):
		return
		tiles = [
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
		]

		random.shuffle(tiles)

		plays = [
			majiang.plays.Eyes()
		]

		finder = majiang.playfinder.PlayFinder(plays)
		finds = finder.find(tiles)

		self.assertEqual(len(finds), 1)
		self.assertIsInstance(finds[0], majiang.plays.Eyes)

	def test_find_one_eyes_among_many(self):
		return
		tiles = [
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
			majiang.tiles.Circle(1),
			majiang.tiles.Circle(2),
			majiang.tiles.Circle(3),
			majiang.tiles.Circle(4),
			majiang.tiles.Circle(5),
			majiang.tiles.Circle(6),
			majiang.tiles.Circle(7),
			majiang.tiles.Circle(9),
			majiang.tiles.Bamboo(1),
			majiang.tiles.Bamboo(2),
			majiang.tiles.Bamboo(3),
		]

		random.shuffle(tiles)

		plays = [
			majiang.plays.Eyes()
		]

		finder = majiang.playfinder.PlayFinder(plays)
		finds = finder.find(tiles)

		self.assertEqual(len(finds), 1)
		self.assertIsInstance(finds[0], majiang.plays.Eyes)

	def test_find_many_eyes(self):
		tiles = [
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
			majiang.tiles.Circle(1),
			majiang.tiles.Circle(1),
			majiang.tiles.Circle(1),
			majiang.tiles.Circle(4),
			majiang.tiles.Circle(5),
			majiang.tiles.Circle(6),
			majiang.tiles.Circle(7),
			majiang.tiles.Circle(8),
			majiang.tiles.Circle(9),
			majiang.tiles.Bamboo(1),
			majiang.tiles.Bamboo(2),
			majiang.tiles.Bamboo(3),
		]

		random.shuffle(tiles)

		plays = [
			majiang.plays.Eyes()
		]

		finder = majiang.playfinder.PlayFinder(plays)
		finds = finder.find(tiles)

		self.assertEqual(len(finds), 3)
		self.assertIsInstance(finds[0], majiang.plays.Eyes)
		self.assertIsInstance(finds[1], majiang.plays.Eyes)
		self.assertIsInstance(finds[2], majiang.plays.Eyes)


	def test_find_one_peng_alone(self):
		return
		tiles = [
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
		]

		random.shuffle(tiles)

		plays = [
			majiang.plays.Peng()
		]

		finder = majiang.playfinder.PlayFinder(plays)
		finds = finder.find(tiles)

		self.assertEqual(len(finds), 1)
		self.assertIsInstance(finds[0], majiang.plays.Peng)

	def test_find_one_peng_among_many(self):
		return
		tiles = [
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
			majiang.tiles.Circle(1),
			majiang.tiles.Circle(2),
			majiang.tiles.Circle(3),
			majiang.tiles.Circle(4),
			majiang.tiles.Circle(5),
			majiang.tiles.Circle(6),
			majiang.tiles.Circle(7),
			majiang.tiles.Circle(9),
			majiang.tiles.Bamboo(1),
			majiang.tiles.Bamboo(2),
			majiang.tiles.Bamboo(3),
		]

		random.shuffle(tiles)

		plays = [
			majiang.plays.Peng()
		]

		finder = majiang.playfinder.PlayFinder(plays)
		finds = finder.find(tiles)

		self.assertEqual(len(finds), 1)
		self.assertIsInstance(finds[0], majiang.plays.Peng)

	def test_find_many_peng(self):
		tiles = [
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
			majiang.tiles.Circle(1),
			majiang.tiles.Circle(1),
			majiang.tiles.Circle(1),
			majiang.tiles.Circle(4),
			majiang.tiles.Circle(5),
			majiang.tiles.Circle(6),
			majiang.tiles.Circle(7),
			majiang.tiles.Circle(8),
			majiang.tiles.Circle(9),
			majiang.tiles.Bamboo(1),
			majiang.tiles.Bamboo(2),
			majiang.tiles.Bamboo(3),
		]

		random.shuffle(tiles)

		plays = [
			majiang.plays.Peng()
		]

		finder = majiang.playfinder.PlayFinder(plays)
		finds = finder.find(tiles)

		self.assertEqual(len(finds), 2)
		self.assertIsInstance(finds[0], majiang.plays.Peng)
		self.assertIsInstance(finds[1], majiang.plays.Peng)

	def test_find_one_chao_alone(self):
		return
		tiles = [
			majiang.tiles.Circle(1),
			majiang.tiles.Circle(2),
			majiang.tiles.Circle(3),
		]

		random.shuffle(tiles)

		plays = [
			majiang.plays.Chao()
		]

		finder = majiang.playfinder.PlayFinder(plays)
		finds = finder.find(tiles)

		self.assertEqual(len(finds), 1)
		self.assertIsInstance(finds[0], majiang.plays.Chao)

	def test_find_one_chao_among_many(self):
		return
		tiles = [
			majiang.tiles.Circle(1),
			majiang.tiles.Circle(2),
			majiang.tiles.Circle(3),
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
			majiang.tiles.Bamboo(1),
			majiang.tiles.Bamboo(2),
			majiang.tiles.Bamboo(5),
		]

		random.shuffle(tiles)

		plays = [
			majiang.plays.Chao()
		]

		finder = majiang.playfinder.PlayFinder(plays)
		finds = finder.find(tiles)

		self.assertEqual(len(finds), 1)
		self.assertIsInstance(finds[0], majiang.plays.Chao)

	def test_find_many_chao(self):
		tiles = [
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
			majiang.tiles.Circle(1),
			majiang.tiles.Circle(2),
			majiang.tiles.Circle(3),
			majiang.tiles.Circle(4),
			majiang.tiles.Circle(5),
			majiang.tiles.Circle(6),
			majiang.tiles.Circle(7),
			majiang.tiles.Circle(8),
			majiang.tiles.Circle(9),
			majiang.tiles.Bamboo(1),
			majiang.tiles.Bamboo(2),
			majiang.tiles.Bamboo(3),
		]

		random.shuffle(tiles)

		plays = [
			majiang.plays.Chao()
		]

		finder = majiang.playfinder.PlayFinder(plays)
		finds = finder.find(tiles)

		self.assertEqual(len(finds), 8)
		for i in range(0, 8):
			self.assertIsInstance(finds[i], majiang.plays.Chao)

	def test_find_chao_with_an_eyes(self):
		tiles = [
			majiang.tiles.Circle(1),
			majiang.tiles.Circle(2),
			majiang.tiles.Circle(2),
			majiang.tiles.Circle(3),
		]

		random.shuffle(tiles)

		plays = [
			majiang.plays.Chao(),
		]

		finder = majiang.playfinder.PlayFinder(plays)
		finds = finder.find(tiles)

		self.assertEqual(len(finds), 1)
		self.assertIsInstance(finds[i], majiang.plays.Chao)
