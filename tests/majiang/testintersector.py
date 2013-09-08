import majiang.tiles
import majiang.intersector
import unittest


class TestIntersector(unittest.TestCase):
    def test_intersect_with(self):
        g = [
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
            majiang.tiles.Bamboo(4),
            majiang.tiles.Bamboo(4),
        ]

        plays = []
        plays.append(
            majiang.plays.Chao([
                g[0], g[1], g[2]
            ])
        )
        plays.append(
            majiang.plays.Eyes([
                g[2], g[3]
            ])
        )

        intersect = majiang.intersector.Intersector()
        intersections = intersect.intersect(plays)

        self.assertEqual(len(intersections), 1)
        self.assertEqual(intersections[0], (plays[0],plays[1], [g[2]]))

    def test_intersect_with_extra(self):
        g = [
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
            majiang.tiles.Bamboo(4),
            majiang.tiles.Bamboo(4),
            majiang.tiles.Bamboo(5),
            majiang.tiles.Bamboo(5),
        ]

        plays = []
        plays.append(
            majiang.plays.Chao([
                g[0], g[1], g[2]
            ])
        )
        plays.append(
            majiang.plays.Eyes([
                g[2], g[3]
            ])
        )

        plays.append(
            majiang.plays.Eyes([
                g[4], g[5]
            ])
        )


        intersect = majiang.intersector.Intersector()
        intersections = intersect.intersect(plays)

        self.assertEqual(len(intersections), 1)
        self.assertEqual(intersections[0], (plays[0],plays[1], [g[2]]))

    def test_intersect_without(self):
        g = [
            majiang.tiles.Bamboo(1),
            majiang.tiles.Bamboo(2),
            majiang.tiles.Bamboo(3),
            majiang.tiles.Bamboo(4),
            majiang.tiles.Bamboo(4),
        ]

        plays = []
        plays.append(
            majiang.plays.Chao([
                g[0], g[1], g[2]
            ])
        )
        plays.append(
            majiang.plays.Eyes([
                g[3], g[4]
            ])
        )

        intersect = majiang.intersector.Intersector()
        intersections = intersect.intersect(plays)

        self.assertEqual(len(intersections), 0)


if __name__ == "__main__":
    unittest.main()
