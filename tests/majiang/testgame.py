import majiang.game
import majiang.player
import unittest
import pprint


class TestGame(unittest.TestCase):
    def test_game_starts_with_zero_players(self):
        g = majiang.game.Game()
        self.assertEqual(g.player_count(), 0)

    def test_game_knows_how_many_players_there_are(self):
        g = majiang.game.Game()
        self.assertEqual(g.player_count(), 0)

        g.add_player(majiang.player.Player("laurence"))
        self.assertEqual(g.player_count(), 1)

        g.add_player(majiang.player.Player("qianqi"))
        self.assertEqual(g.player_count(), 2)

        g.add_player(majiang.player.Player("liangpei"))
        self.assertEqual(g.player_count(), 3)

        g.add_player(majiang.player.Player("cute-lam"))
        self.assertEqual(g.player_count(), 4)

    def test_game_cannot_have_more_than_four_players(self):
        g = majiang.game.Game()
        self.assertEqual(g.player_count(), 0)
        self.assertTrue(g.add_player(majiang.player.Player("laurence")))
        self.assertTrue(g.add_player(majiang.player.Player("qianqi")))
        self.assertTrue(g.add_player(majiang.player.Player("liangpei")))
        self.assertTrue(g.add_player(majiang.player.Player("cute-lam")))

        self.assertRaises(Exception, g.add_player, (majiang.player.Player("unwanted-player")))

    def test_game_get_player_returns_player_object_when_no_ref(self):
        g = majiang.game.Game()
        g.add_player(majiang.player.Player("laurence"))
        g.add_player(majiang.player.Player("qianqi"))
        g.add_player(majiang.player.Player("liangpei"))
        g.add_player(majiang.player.Player("cute-lam"))

        self.assertEqual(type(g._get_player()), majiang.player.Player)

    def test_game_get_player_returns_player_index_when_object_ref(self):
        g = majiang.game.Game()
        me = majiang.player.Player("laurence")
        g.add_player(me)
        g.add_player(majiang.player.Player("qianqi"))
        g.add_player(majiang.player.Player("liangpei"))
        g.add_player(majiang.player.Player("cute-lam"))

        self.assertEqual(type(g._get_player(me)), int)

    def test_game_get_player_returns_player_object_when_index_ref(self):
        g = majiang.game.Game()
        me = majiang.player.Player("laurence")
        g.add_player(me)
        g.add_player(majiang.player.Player("qianqi"))
        g.add_player(majiang.player.Player("liangpei"))
        g.add_player(majiang.player.Player("cute-lam"))

        # don't test on me, because I might shuffle players sooner one day
        self.assertEqual(type(g._get_player(0)), majiang.player.Player)



if __name__ == "__main__":
    unittest.main()
