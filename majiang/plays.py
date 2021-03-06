class Play(object):
    def __init__(self, tiles=None):
        if tiles is not None:
            if self.match(tiles):
                self._tiles = tiles
            else:
                raise Exception("Play:__init__:mismatch")

    def get_tiles(self):
        return self._tiles

    def _get_values(self, tiles):
        values = []
        for t in tiles:
            values.append(t.get_value())
        return values

    def _get_types(self, tiles):
        types = []
        for t in tiles:
            types.append(t.get_type())
        return types

    def types_are_equal(self, tiles):
        types = self._get_types(tiles)
        return len(set(types)) == 1

    def values_are_equal(self, tiles):
        values = self._get_values(tiles)
        return len(set(values)) == 1

    def values_are_sequential(self, tiles):
        values = self._get_values(tiles)

        # all values must be unique
        if len(set(values)) < len(values):
            return False

        if max(values) == (min(values) + len(values) - 1):
            return True

        return False

    def contains(self, tiles):
        if type(tiles) is not list:
            tiles = [tiles]

        tile_set_1 = set(self._tiles)
        tile_set_2 = set(tiles)

        return list(tile_set_1.intersection(tile_set_2))

    def get_type(self):
        # This only works because a play is *ALWAYS* of the same type
        return self._tiles[0].get_type()


class Eyes(Play):
    def tile_count(self):
        return 2

    def match(self, tiles):
        if not len(tiles) == 2:
            return False

        if not self.types_are_equal(tiles):
            return False

        if not self.values_are_equal(tiles):
            return False

        return True


class Peng(Play):
    def tile_count(self):
        return 3

    def match(self, tiles):
        if len(tiles) != 3:
            return False

        if self.types_are_equal(tiles) and self.values_are_equal(tiles):
            return True
        else:
            return False


class Chao(Play):
    def tile_count(self):
        return 3

    def match(self, tiles):
        if not len(tiles) == 3:
            return False

        if not tiles[0].can_chao():
            return False

        if not self.types_are_equal(tiles):
            return False

        if not self.values_are_sequential(tiles):
            return False

        return True


class Sequence(Play):
    def tile_count(self):
        return len(self._tiles)

    def match(self, tiles):
        if len(tiles) < 2:
            return False

        if not self.types_are_equal(tiles):
            return False

        if not self.values_are_sequential(tiles):
            return False

        return True

    def min(self):
        d = [tile.get_value() for i, tile in enumerate(self._tiles)]
        return min(d)

    def max(self):
        d = [tile.get_value() for i, tile in enumerate(self._tiles)]
        return max(d)


class Kong(Play):
    def tile_count(self):
        return 4

    def match(self, tiles):
        if not len(tiles) == 4:
            return False

        if not self.types_are_equal(tiles):
            return False

        if not self.values_are_equal(tiles):
            return False

        return True


class Majiang(Play):
    def match(self, plays):
        tiles = []
        [tiles.extend(p.get_tiles()) for p in plays]

        # Can't use a tile more than once
        unique = list(set(tiles))
        if len(unique) != len(tiles):
            return False

        # No Majiang can have more than 15 tiles
        if len(tiles) > 15:
            return False

        # No Majiang can have less than 14 tiles
        if len(tiles) < 14:
            return False

        types = [type(p) for p in plays]

        # All Majiangs must include one pair
        if types.count(Eyes) != 1:
            return False

        # All majiangs must include 4 sets
        if (types.count(Peng) + types.count(Chao) + types.count(Kong)) != 4:
            return False

        return True
