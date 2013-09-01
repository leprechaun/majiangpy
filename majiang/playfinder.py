import majiang.tiles


class PlayFinder(object):
    def __init__(self, plays=[]):
        self._plays = plays

    def bucket_tiles(self,tiles):
        tiles = self.sort_tiles(tiles)

        buckets = {}
        for t in tiles:
            if not t.get_type() in buckets:
                buckets[t.get_type()] = {}

            if not t.get_value() in buckets[t.get_type()]:
                buckets[t.get_type()][t.get_value()] = []

            buckets[t.get_type()][t.get_value()].append(t)

        return buckets

    def find(self, tiles):
        plays = []
        buckets = self.bucket_tiles(tiles)

        for t in buckets.keys():
            for v in range(1, 10):
                # LOL. Look at my AlmostChao test ...
                if not v in buckets[t]:
                    continue

                # Kong / Should I also return a Peng? Perhaps I need a PlaySet class
                if len(buckets[t][v]) == 4:
                    plays.append(majiang.plays.Kong(buckets[t][v]))

                # Peng / Should I also return a Eyes? Perhaps I need a PlaySet class ...
                if len(buckets[t][v]) == 3:
                    plays.append(majiang.plays.Peng(buckets[t][v]))

                # Eyes
                if len(buckets[t][v]) == 2:
                    plays.append(majiang.plays.Eyes(buckets[t][v]))

                # An "AlmostEyes" would be useless ...

                """
                What I need done here is ... identify chaos

                Loop through possible values, and see when I have [v, v+1, v+2]
                But I also have AlmostChaos, that's when I see [v, v+1] or [v, v+2]

                The difficulty lies in identifying more than one ... why?
                """
                # Chao / Wind and Dragons can't
                if t != "wind" and t != "dragon":
                    # Backup the bucket so I can fuck it up
                    bucket = buckets[t]
                    if v in buckets[t] and v+1 in buckets[t] and v+2 in buckets[t]:
                        chao_count = min([
                            len(buckets[t][v]),
                            len(buckets[t][v+1]),
                            len(buckets[t][v+2]),
                        ])

                        for i in range(0, chao_count):
                            plays.append(
                                majiang.plays.Chao([
                                    buckets[t][v][i],
                                    buckets[t][v+1][i],
                                    buckets[t][v+2][i]
                                ])
                            )
                    elif v in buckets[t] and v+1 in buckets[t] and v-1 not in buckets[t]:
                        chao_count = min([
                            len(buckets[t][v]),
                            len(buckets[t][v+1])
                        ])

                        for i in range(0, chao_count):
                            plays.append(
                                majiang.plays.AlmostChao([
                                    buckets[t][v][i],
                                    buckets[t][v+1][i],
                                ])
                            )

                    elif v in buckets[t] and v+2 in buckets[t] and v+1 not in buckets[t]:
                        # I'll need to do something here ...
                        True

        return plays

    def _find(self, tiles):
        tiles = self.sort_tiles(tiles)
        found_plays = []
        for p in self._plays:
            for i in range(0, len(tiles)-(p.tile_count()-1)):
                tgroup = tiles[i:i+(p.tile_count())]
                if p.match(tgroup):
                    found_plays.append(type(p)(tgroup))
                    #print("Match:", str(tgroup[0]), str(tgroup[1]), str(tgroup[2]))
                else:
                    True
                    #print("No:", str(tgroup[0]), str(tgroup[1]), str(tgroup[2]))

        return found_plays

    def sort_tiles(self, tiles):
        d = [(tile.get_type(), tile.get_value(), i, tile) for i, tile in enumerate(tiles)]    
        d.sort()
        return [tile for t, v, i, tile in d]
