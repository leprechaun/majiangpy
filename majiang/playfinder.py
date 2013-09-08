import majiang.tiles


class PlayFinder(object):
    def __init__(self, plays=[]):
        self._plays = plays

    def find(self, tiles, find_sames=True, find_sequences=True):
        plays = []
        buckets = self.bucket_tiles(tiles)
        for t in buckets:
            if find_sames:
                plays = plays + self.find_sames(buckets[t])

            if find_sequences:
                if t not in ["wind", "dragon"]:
                    plays = plays + self.find_sequences(buckets[t])

        return plays

    def find_sames(self, bucket):
        plays = []
        for v in bucket:
            p = None
            if len(bucket[v]) == 2:
                p = majiang.plays.Eyes(bucket[v].copy())
            elif len(bucket[v]) == 3:
                p = majiang.plays.Peng(bucket[v].copy())
            elif len(bucket[v]) == 4:
                p = majiang.plays.Kong(bucket[v].copy())

            if p is not None:
                plays.append(p)

        return plays

    def find_sequences(self, bucket):
        plays = []
        current_sequence = []

        # Go up to 10 just so we hit the else and close/append the sequence
        while bucket != {}:
            for i in range(1, 11):
                if i in bucket:
                    current_sequence.append(bucket[i].pop())
                    if bucket[i] == []:
                        bucket.pop(i)
                else:
                    if len(current_sequence) < 2:
                        current_sequence = []
                    else:
                        sequence = majiang.plays.Sequence(current_sequence)
                        plays.append(sequence)
                        current_sequence = []

        return plays

    def sort_tiles(self, tiles):
        d = [(tile.get_type(), tile.get_value(), i, tile) for i, tile in enumerate(tiles)]
        d.sort()
        return [tile for t, v, i, tile in d]

    def bucket_tiles(self, tiles):
        tiles = self.sort_tiles(tiles)

        buckets = {}
        for t in tiles:
            if not t.get_type() in buckets:
                buckets[t.get_type()] = {}

            if not t.get_value() in buckets[t.get_type()]:
                buckets[t.get_type()][t.get_value()] = []

            buckets[t.get_type()][t.get_value()].append(t)

        return buckets
