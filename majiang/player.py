import random


class Player(object):
    def __init__(self, name):
        self._name = name
        self._tiles = []

    def intake_initial_tiles(self, tiles):
        for t in tiles:
            self._tiles.append(t)

        self._inplace_sort()

        s = [(t.get_type() + "-" + str(t.get_value())) for t in self._tiles]
        print(self.get_name() + " just drawed, got these:")
        print("    ", ", ".join(s))

    def intake_draw(self, tile):
        s = [(t.get_type() + "-" + str(t.get_value())) for t in self._tiles]
        s = ",".join(s)

        random.shuffle(self._tiles)
        discard = self._tiles.pop()
        self._tiles.append(tile)

        print(self.get_name(), "has:", s)
        print(self.get_name(), "drew:", tile)
        print(self.get_name(), "discarded:", discard)
        print("")
        return tile

    def intake_discard(self, tile):
        #self._tiles.append(tile)
        return tile

    def get_name(self):
        return self._name

    def _inplace_sort(self):
        self._tiles = self._sort_tiles(self._tiles)

    def _sort_tiles(self, tiles):
        d = [(tile.get_type(), tile.get_value(), i, tile) for i, tile in enumerate(tiles)]
        d.sort()
        return [tile for t, v, i, tile in d]

def PlayerInterface(object):
    def __init__(self, name):
        self._name = name

    def offer_draw(self, tile):
        return True

    def offer_discard(self, tile):
        return True

    def sdfsf(self):
        return True
