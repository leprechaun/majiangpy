import majiang.tiles
import majiang.plays
import unittest


class TestPlays(unittest.TestCase):
    def test_play_same_values_pass(self):
        t = [
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(1)
        ]

        play = majiang.plays.Play()
        self.assertEqual(play.values_are_equal(t), True)

    def test_play_same_value_fail(self):
        t = [
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(2)
        ]

        play = majiang.plays.Play()
        self.assertEqual(play.values_are_equal(t), False)

    def test_play_sequential_values_pass(self):
        t = [
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(2),
            majiang.tiles.Dragon(3)
        ]

        play = majiang.plays.Play()
        self.assertEqual(play.values_are_sequential(t), True)

    def test_play_sequential_values_fail(self):
        t = [
            majiang.tiles.Dragon(1),
            majiang.tiles.Dragon(2),
            majiang.tiles.Dragon(2)
        ]

        play = majiang.plays.Play()
        self.assertEqual(play.values_are_sequential(t), False)

    def test_play_same_types_pass(self):
        pass

    def test_play_same_types_fail(self):
        pass

    def test_plays_constructor_detects_mismatches(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Circle(2))

        self.assertRaises(Exception, majiang.plays.Sequence, (p))



class TestEyes(unittest.TestCase):
    def test_eyes_match(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))

        eyes = majiang.plays.Eyes()
        self.assertEqual(eyes.match(p), True)

    def test_eyes_non_match_not_same_value(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(2))

        eyes = majiang.plays.Eyes()
        self.assertEqual(eyes.match(p), False)

    def test_eyes_non_match_not_same_type(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Wind(1))

        eyes = majiang.plays.Eyes()
        self.assertEqual(eyes.match(p), False)

    def test_eyes_non_match_not_right_count_over(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))

        eyes = majiang.plays.Eyes()
        self.assertEqual(eyes.match(p), False)

    def test_eyes_non_match_not_right_count_under(self):
        p = []
        p.append(majiang.tiles.Dragon(1))

        eyes = majiang.plays.Eyes()
        self.assertEqual(eyes.match(p), False)


class TestPeng(unittest.TestCase):
    def test_peng_match(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))

        peng = majiang.plays.Peng()
        self.assertEqual(peng.match(p), True)

    def test_peng_non_match_not_same_value(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(2))

        peng = majiang.plays.Peng()
        self.assertEqual(peng.match(p), False)

    def test_peng_non_match_not_same_type(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Wind(2))

        peng = majiang.plays.Peng()
        self.assertEqual(peng.match(p), False)

    def test_peng_non_match_not_right_count_over(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))

        peng = majiang.plays.Peng()
        self.assertEqual(peng.match(p), False)

    def test_peng_non_match_not_right_count_under(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))

        peng = majiang.plays.Peng()
        self.assertEqual(peng.match(p), False)


class TestKong(unittest.TestCase):
    def test_kong_match(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))

        kong = majiang.plays.Kong()
        self.assertEqual(kong.match(p), True)

    def test_kong_non_match_not_same_value(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(2))
        p.append(majiang.tiles.Dragon(2))

        kong = majiang.plays.Kong()
        self.assertEqual(kong.match(p), False)

    def test_kong_non_match_not_same_type(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Wind(2))
        p.append(majiang.tiles.Wind(2))

        kong = majiang.plays.Kong()
        self.assertEqual(kong.match(p), False)

    # not that this could actually happen.
    def test_kong_non_match_not_right_count_over(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))

        kong = majiang.plays.Kong()
        self.assertEqual(kong.match(p), False)

    def test_peng_non_match_not_right_count_under(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(1))

        kong = majiang.plays.Kong()
        self.assertEqual(kong.match(p), False)


class TestChao(unittest.TestCase):
    def test_chao_match(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))
        p.append(majiang.tiles.Bamboo(3))

        chao = majiang.plays.Chao()
        self.assertEqual(chao.match(p), True)

    def test_chao_non_match_not_sequential_values(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))
        p.append(majiang.tiles.Bamboo(4))

        chao = majiang.plays.Chao()
        self.assertEqual(chao.match(p), False)

    def test_chao_non_match_not_same_type(self):
        p = []
        p.append(majiang.tiles.Circle(1))
        p.append(majiang.tiles.Bamboo(2))
        p.append(majiang.tiles.Bamboo(3))

        chao = majiang.plays.Chao()
        self.assertEqual(chao.match(p), False)

    def test_chao_non_match_non_chaoable_type_dragon(self):
        p = []
        p.append(majiang.tiles.Dragon(1))
        p.append(majiang.tiles.Dragon(2))
        p.append(majiang.tiles.Dragon(3))

        chao = majiang.plays.Chao()
        self.assertEqual(chao.match(p), False)

    def test_chao_non_match_non_chaoable_type_wind(self):
        p = []
        p.append(majiang.tiles.Wind(1))
        p.append(majiang.tiles.Wind(2))
        p.append(majiang.tiles.Wind(3))

        chao = majiang.plays.Chao()
        self.assertEqual(chao.match(p), False)

    def test_chao_non_match_not_right_count_over(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))
        p.append(majiang.tiles.Bamboo(3))
        p.append(majiang.tiles.Bamboo(3))

        chao = majiang.plays.Chao()
        self.assertEqual(chao.match(p), False)

    def test_chao_non_match_not_right_count_under(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))

        chao = majiang.plays.Chao()
        self.assertEqual(chao.match(p), False)


class TestSequence(unittest.TestCase):
    def test_match(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))

        sequence = majiang.plays.Sequence(p)
        self.assertEqual(sequence.match(p), True)

    def test_non_match_type(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))
        p.append(majiang.tiles.Circle(3))

        sequence = majiang.plays.Sequence()
        self.assertEqual(sequence.match(p), False)

    def test_non_match_values(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))
        p.append(majiang.tiles.Bamboo(4))

        sequence = majiang.plays.Sequence()
        self.assertEqual(sequence.match(p), False)

    def test_tile_count_0(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))

        sequence = majiang.plays.Sequence()
        self.assertEqual(sequence.match(p), False)

    def test_tile_count_1(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))
        p.append(majiang.tiles.Bamboo(3))

        sequence = majiang.plays.Sequence(p)
        self.assertEqual(sequence.match(p), True)

        self.assertEqual(sequence.tile_count(), 3)

    def test_tile_count_2(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))
        p.append(majiang.tiles.Bamboo(3))
        p.append(majiang.tiles.Bamboo(4))

        sequence = majiang.plays.Sequence(p)
        self.assertEqual(sequence.match(p), True)

        self.assertEqual(sequence.tile_count(), 4)

    def test_tile_min_max(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))
        p.append(majiang.tiles.Bamboo(3))
        p.append(majiang.tiles.Bamboo(4))

        sequence = majiang.plays.Sequence(p)
        self.assertEqual(sequence.min(), 1)
        self.assertEqual(sequence.max(), 4)

    def test_play_contains_single_tile(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))
        p.append(majiang.tiles.Bamboo(3))
        p.append(majiang.tiles.Bamboo(4))

        sequence = majiang.plays.Sequence(p)
        self.assertEqual(sequence.contains(p[0]), [p[0]])

    def test_play_contains_single_array(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))
        p.append(majiang.tiles.Bamboo(3))
        p.append(majiang.tiles.Bamboo(4))

        sequence = majiang.plays.Sequence(p)
        self.assertEqual(sequence.contains([p[0]]), [p[0]])

    def test_play_contains_multiple_array(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))
        p.append(majiang.tiles.Bamboo(3))
        p.append(majiang.tiles.Bamboo(4))

        sequence = majiang.plays.Sequence(p)
        self.assertEqual(set(sequence.contains([p[0], p[1]])), set([p[0], p[1]]))

    def test_play_contains_no_match(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))
        p.append(majiang.tiles.Bamboo(3))
        p.append(majiang.tiles.Bamboo(4))

        sequence = majiang.plays.Sequence(p)
        self.assertEqual(sequence.contains(majiang.tiles.Bamboo(1)), [])

    def test_plays_returns_its_type(self):
        p = []
        p.append(majiang.tiles.Bamboo(1))
        p.append(majiang.tiles.Bamboo(2))

        sequence = majiang.plays.Sequence(p)
        self.assertEqual(sequence.get_type(), "bamboo")


if __name__ == "__main__":
    unittest.main()
