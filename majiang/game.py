import random
import majiang.cemetary


class Game:
    def __init__(self, players=None, wall=None, accountant=None, cemetary=None):
        # players at construct
        if type(players) == list:
            if not len(players) == 4:
                raise Exception("Not right about of players")
            else:
                self._players = players
        # or players via add_player
        else:
            self._players = []

        if not type(wall) is None:
            self._wall = wall

        if not type(accountant) == majiang.accountant.Accountant:
            self._accountant = majiang.accountant.Accountant()
        else:
            self._accountant = accountant

        if not type(cemetary) == majiang.cemetary.Cemetary:
            self._cemetary = majiang.cemetary.Cemetary()
        else:
            self._cemetary = cemetary

        self._current_turn_player_index = 0
        self._log = []

        return

    def add_player(self, player):
        if len(self._players) < 4:
            self._players.append(player)
        else:
            raise Exception

        return True

    def player_count(self):
        return len(self._players)

    def start(self):
        if self.player_count() != 4:
            raise Exception("Not enough players")

        # Randomise the players order
        self._shuffle_players()

        # Assign initial tiles to players
        self._assign_initial_tiles()

        self._enter_game_loop()

    def _enter_game_loop(self):
        while not self._game_won() and self._wall.tiles_left() > 0:
            player = self._get_player()
            self._take_turn(player)

    def _take_turn(self, player):
        tile = self._wall.draw_tile()

        discard = player.intake_draw(tile)

        play = self._offer_discard_to_other_players(discard)
        if play is not None:
            pass

        self._inc_player()

    def _offer_discard_to_other_players(self, discard_tile):
        # E, S, W, N
        order = [0, 1, 2, 3]

        # Lets not bother offering a tile to the player who discards it
        # first returns current turn player instance
        # second returns its index
        order.remove(self._get_player(self._get_player()))

        # Just to make thigs a little more fair
        random.shuffle(order)

        # in the order we decided, go through the discard offering dance
        for i in order:
            # get player instance
            p = self._get_player(i)

            # offer the card
            play = p.intake_discard(discard_tile)

            # expect a Play, or None
            if isinstance(play, majiang.plays.Play):
                # validate player has the tiles in play
                if self._accountant.has_tiles(p, play.get_tiles()):
                    self._set_player(p)
                    self._offer_discard_to_other_players(new_discard)
                    break
                else:
                    raise Exception("Player instantiated a tile! Cheater!")

    def _assign_initial_tiles(self):
        for p in self._players:
            # traditionally East gets 14 tiles and doesn't draw first turn
            # but, really, this ends up the same

            # draw 13 tiles
            tiles = self._wall.draw_tile(13)

            # make sure we can account for those tiles
            tiles = self._accountant.add_tiles(p, tiles)

            # actually give them to the player
            p.intake_initial_tiles(tiles)

    def _shuffle_players(self):
        random.shuffle(self._players)

    def _set_player(self, ref):
        if ref in [0, 1, 2, 3]:
            self._current_turn_player_index = ref
        else:
            self._current_turn_player_index = self._get_player(player)

    def _inc_player(self):
        i = self._get_player(self._get_player())
        i = i + 1
        i = i % 4

        self._set_player(i)

    # Method to return players or get their index
    def _get_player(self, ref=None):
        # Current player requested
        if ref is None:
            return self._players[self._current_turn_player_index]

        # If giving an index, return the player object
        elif ref in [0, 1, 2, 3]:
            return self._players[ref]

        # If giving a player object, return the index
        elif type(ref) == majiang.player.Player:
            return self._players.index(ref)

        else:
            raise Exception("Unknown player ref type")

    def _game_won(self):
        return False

    def log(self, text):
        print(text)
'''
add players
init wall
assign tiles

1 - get turn player index
2 - offer player i tile
3 - accept player i discard
4 - offer player i discard to others
5 - if accept and valid play
5.a - accept player j discard
5.b - i = j
6 - i++ & goto 1

def offer_discard( player, tile ):
    for p in randomized_players:
        if play = p.offer_discard(tile):
            if Play.is_valid(play)
                self._current_player_idex = get_index( p )
                discard = p.get_discard()
                offer_discard( p, discard )
'''
