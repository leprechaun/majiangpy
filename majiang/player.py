class Player:
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
        print(self.get_name(), ": has ", s)
        print( self.get_name(), ": got ", tile )
        print( self.get_name(), ": discarded ", tile )
        return tile

    def intake_discard(self, tile):
        self._tiles.append(tile)

    def get_name(self):
        return self._name

    def _inplace_sort(self):
        self._tiles = self._sort_tiles(self._tiles)

    def _sort_tiles(self, tiles):
        d = [(tile.get_type(), tile.get_value(), i, tile) for i, tile in enumerate(tiles)]    
        d.sort()
        return [tile for t, v, i, tile in d]
