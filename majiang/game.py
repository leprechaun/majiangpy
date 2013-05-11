class Game:
	_players = []
	def __init__(self):
		self._players = []
		return

	def add_player(self, player):
		if len( self._players ) < 4:
			self._players.append( player )
		else:
			raise Exception

		return True

	def player_count( self ):
		return len( self._players )
