import majiang.tiles
import majiang.plays
import majiang.playfinder
import majiang.wall


w = majiang.wall.Wall()
tiles = [
    majiang.tiles.Bamboo(1),
    majiang.tiles.Bamboo(2),
    majiang.tiles.Bamboo(3),
    majiang.tiles.Bamboo(2),
    majiang.tiles.Bamboo(3),
]


tiles = w.draw_tile(14)


pd = majiang.playfinder.PlayFinder()

finds = pd.find(tiles)


def print_tiles(tiles):
    strings = []
    for t in tiles:
        strings.append(str(t))
    strings.sort()
    return (",".join(strings)) + "\n"

print(print_tiles(tiles))

for find in finds:
    print(find)
    print(print_tiles(find.get_tiles()))
