import majiang.tiles
import majiang.plays
import unittest

class TestPlays(unittest.TestCase):
	def test_play_same_values_pass(self):
		t = [
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1)
		]

		play = majiang.plays.Play()
		self.assertEqual(play.values_are_equal(t),True)

	def test_play_same_value_fail(self):
		t = [
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(2)
		]

		play = majiang.plays.Play()
		self.assertEqual(play.values_are_equal(t),False)


	def test_play_sequential_values_pass(self):
		t = [
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(2),
			majiang.tiles.Dragon(3)
		]

		play = majiang.plays.Play()
		self.assertEqual(play.values_are_sequential(t),True)

	def test_play_sequential_values_fail(self):
		t = [
			majiang.tiles.Dragon(1),
			majiang.tiles.Dragon(2),
			majiang.tiles.Dragon(2)
		]

		play = majiang.plays.Play()
		self.assertEqual(play.values_are_sequential(t),False)

	def test_play_same_types_pass(self):
		pass

	def test_play_same_types_fail(self):
		pass

class TestPair(unittest.TestCase):
	def test_pair_match(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )

		pair = majiang.plays.Pair()
		self.assertEqual( pair.match( p ), True )

	def test_peng_non_match_not_same_value(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(2) )

		pair = majiang.plays.Pair()
		self.assertEqual( pair.match( p ), False )

	def test_peng_non_match_not_same_type(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Wind(1) )

		pair = majiang.plays.Pair()
		self.assertEqual( pair.match( p ), False )

	def test_peng_non_match_not_right_count_over(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )

		pair = majiang.plays.Pair()
		self.assertEqual( pair.match( p ), False )

	def test_peng_non_match_not_right_count_under(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )

		pair = majiang.plays.Pair()
		self.assertEqual( pair.match( p ), False )

class TestPeng(unittest.TestCase):
	def test_peng_match(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )

		peng = majiang.plays.Peng()
		self.assertEqual( peng.match( p ), True )

	def test_peng_non_match_not_same_value(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(2) )

		peng = majiang.plays.Peng()
		self.assertEqual( peng.match( p ), False )

	def test_peng_non_match_not_same_type(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Wind(2) )

		peng = majiang.plays.Peng()
		self.assertEqual( peng.match( p ), False )

	def test_peng_non_match_not_right_count_over(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )

		peng = majiang.plays.Peng()
		self.assertEqual( peng.match( p ), False )

	def test_peng_non_match_not_right_count_under(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )

		peng = majiang.plays.Peng()
		self.assertEqual( peng.match( p ), False )


class TestKong(unittest.TestCase):
	def test_kong_match(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )

		kong = majiang.plays.Kong()
		self.assertEqual( kong.match( p ), True )

	def test_kong_non_match_not_same_value(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(2) )
		p.append( majiang.tiles.Dragon(2) )

		kong = majiang.plays.Kong()
		self.assertEqual( kong.match( p ), False )

	def test_kong_non_match_not_same_type(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Wind(2) )
		p.append( majiang.tiles.Wind(2) )

		kong = majiang.plays.Kong()
		self.assertEqual( kong.match( p ), False )

	# not that this could actually happen.
	def test_kong_non_match_not_right_count_over(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )

		kong = majiang.plays.Kong()
		self.assertEqual( kong.match( p ), False )

	def test_peng_non_match_not_right_count_under(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(1) )

		kong = majiang.plays.Kong()
		self.assertEqual( kong.match( p ), False )

class TestChao(unittest.TestCase):
	def test_chao_match(self):
		p = []
		p.append( majiang.tiles.Bamboo(1) )
		p.append( majiang.tiles.Bamboo(2) )
		p.append( majiang.tiles.Bamboo(3) )

		chao = majiang.plays.Chao()
		self.assertEqual( chao.match( p ), True )

	def test_chao_non_match_not_sequential_values(self):
		p = []
		p.append( majiang.tiles.Bamboo(1) )
		p.append( majiang.tiles.Bamboo(2) )
		p.append( majiang.tiles.Bamboo(4) )

		chao = majiang.plays.Chao()
		self.assertEqual( chao.match( p ), False )

	def test_chao_non_match_not_same_type(self):
		p = []
		p.append( majiang.tiles.Circle(1) )
		p.append( majiang.tiles.Bamboo(2) )
		p.append( majiang.tiles.Bamboo(3) )

		chao = majiang.plays.Chao()
		self.assertEqual( chao.match( p ), False )

	def test_chao_non_match_non_chaoable_type_dragon(self):
		p = []
		p.append( majiang.tiles.Dragon(1) )
		p.append( majiang.tiles.Dragon(2) )
		p.append( majiang.tiles.Dragon(3) )

		chao = majiang.plays.Chao()
		self.assertEqual( chao.match( p ), False )

	def test_chao_non_match_non_chaoable_type_wind(self):
		p = []
		p.append( majiang.tiles.Wind(1) )
		p.append( majiang.tiles.Wind(2) )
		p.append( majiang.tiles.Wind(3) )

		chao = majiang.plays.Chao()
		self.assertEqual( chao.match( p ), False )

	def test_chao_non_match_not_right_count_over(self):
		p = []
		p.append( majiang.tiles.Bamboo(1) )
		p.append( majiang.tiles.Bamboo(2) )
		p.append( majiang.tiles.Bamboo(3) )
		p.append( majiang.tiles.Bamboo(3) )

		chao = majiang.plays.Chao()
		self.assertEqual( chao.match( p ), False )

	def test_chao_non_match_not_right_count_under(self):
		p = []
		p.append( majiang.tiles.Bamboo(1) )
		p.append( majiang.tiles.Bamboo(2) )

		chao = majiang.plays.Chao()
		self.assertEqual( chao.match( p ), False )


if __name__ == "__main__":
	unittest.main()
