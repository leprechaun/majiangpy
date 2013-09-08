class Intersector(object):
    def intersect(self, plays):
        # There must be a better way of doing this.
        # nested loop ... ugh
        comparisons = []
        intersections = []
        for p1 in plays:
            for p2 in plays:
                if p1 == p2:
                    continue

                if set([p1, p2]) in comparisons:
                    continue

                comparisons.append(set([p1, p2]))

                tile_set_one = set(p1.get_tiles())
                tile_set_two = set(p2.get_tiles())

                # The actual comparison
                intersect = list(tile_set_one.intersection(tile_set_two))
                if len(intersect) > 0:
                    intersections.append((p1, p2, intersect))

        return intersections
