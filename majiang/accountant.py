class Accountant(object):
    def __init__(self):
        self._player_tiles = {}
        pass

    def add_tile(self, player, tile):
        self.add_tiles(player, [tile])
        return tile

    def add_tiles(self, player, tiles):
        if player.get_name() not in self._player_tiles:
            self._player_tiles[player.get_name()] = []
        for tile in tiles:
            self._player_tiles[player.get_name()].append(tile)
        return tiles

    def remove_tile(self, player, tile):
        if self.has_tile(player, tile):
            self._player_tiles[player.get_name()].remove(tile)
        else:
            raise Exception("Player doesnt have tile")
        return tile

    def has_tile(self, player, tile):
        if tile in self._player_tiles[player.get_name()]:
            return True
        else:
            return False

    def has_tiles(self, player, tiles):
        r = True
        for t in tiles:
            if not self.has_tile(player, t):
                r = False
        return r
