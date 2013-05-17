import majiang.accountant
import majiang.player
import majiang.tiles
import unittest
import pprint

class TestAccountant(unittest.TestCase):
	def test_accountant_add_tile_returns_the_tile(self):
		a = majiang.accountant.Accountant()
		p = majiang.player.Player("laurence")
		t = majiang.tiles.Dragon( 1 )
		
		self.assertEqual( a.add_tile(p,t), t )

	def test_accountant_take_tile_returns_the_tile(self):
		a = majiang.accountant.Accountant()
		p = majiang.player.Player("laurence")
		t = majiang.tiles.Dragon( 1 )
		
		a.add_tile(p,t)
		self.assertEqual( a.remove_tile(p,t), t )

	def test_accountant_identifies_present_tile(self):
		a = majiang.accountant.Accountant()
		p = majiang.player.Player("laurence")
		t1 = majiang.tiles.Dragon( 1 )
		t2 = majiang.tiles.Dragon( 2 )

		a.add_tile(p,t1)
		a.add_tile(p,t2)

		self.assertEqual( a.has_tile(p,t1), True )
		self.assertEqual( a.has_tile(p,t2), True )

	def test_accountant_identified_non_present_removed_tile(self):
		a = majiang.accountant.Accountant()
		p = majiang.player.Player("laurence")
		t1 = majiang.tiles.Dragon( 1 )
		t2 = majiang.tiles.Dragon( 2 )

		a.add_tile(p,t1)
		self.assertEqual( a.has_tile(p,t1), True )

		a.remove_tile(p,t1)
		self.assertEqual( a.has_tile(p,t1), False )

	def test_accountant_identifies_non_present_tile(self):
		a = majiang.accountant.Accountant()
		p = majiang.player.Player("laurence")
		t1 = majiang.tiles.Dragon( 1 )
		t2 = majiang.tiles.Dragon( 2 )

		a.add_tile(p,t1)

		self.assertEqual( a.has_tile(p,t1), True )
		self.assertEqual( a.has_tile(p,t2), False )

	def test_accountant_identifies_present_tiles(self):
		a = majiang.accountant.Accountant()
		p = majiang.player.Player("laurence")
		t1 = majiang.tiles.Dragon( 1 )
		t2 = majiang.tiles.Dragon( 2 )

		a.add_tile(p,t1)
		a.add_tile(p,t2)

		self.assertEqual( a.has_tiles(p,[t1]), True )

	def test_accountant_identifies_non_present_tiles(self):
		a = majiang.accountant.Accountant()
		p = majiang.player.Player("laurence")
		t1 = majiang.tiles.Dragon( 1 )
		t2 = majiang.tiles.Dragon( 2 )

		a.add_tile(p,t1)

		self.assertEqual( a.has_tiles(p,[t1,t2]), False )


	def test_accountant_raises_exception_when_removing_non_present_tile(self):
		a = majiang.accountant.Accountant()
		p = majiang.player.Player("laurence")
		t1 = majiang.tiles.Dragon( 1 )
		t2 = majiang.tiles.Dragon( 2 )

		a.add_tile(p,t1)

		self.assertRaises( Exception, a.remove_tile, (p,t2) )



if __name__ == "__main__":
	unittest.main()
