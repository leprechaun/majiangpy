import majiang.game
import unittest
import pprint

class TestGame(unittest.TestCase):
	def test_game_starts_with_zero_players(self):
		g = majiang.game.Game()
		self.assertEqual( g.player_count(), 0 )

	def test_game_knows_how_many_players_there_are(self):
		g = majiang.game.Game()
		self.assertEqual( g.player_count(), 0 )

		g.add_player( "laurence" )
		self.assertEqual( g.player_count(), 1 )

		g.add_player( "qianqi" )
		self.assertEqual( g.player_count(), 2 )

		g.add_player( "liangpei" )
		self.assertEqual( g.player_count(), 3 )

		g.add_player( "cute-lam" )
		self.assertEqual( g.player_count(), 4 )

	def test_game_cannot_have_more_than_four_players(self):
		g = majiang.game.Game()
		self.assertEqual( g.player_count(), 0 )
		self.assertTrue( g.add_player("laurence") )
		self.assertTrue( g.add_player("qianqi") )
		self.assertTrue( g.add_player("liangpeu") )
		self.assertTrue( g.add_player("cute-lam") )
		self.assertRaises( Exception, g.add_player, ("unknown player") )

if __name__ == "__main__":
	unittest.main()
